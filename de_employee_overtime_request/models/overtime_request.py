from odoo import fields, models, api, _
from odoo.exceptions import UserError
from datetime import datetime
from odoo.exceptions import Warning

   
class Overtime_MenuForm(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _name='employee.overtime'
    _description="OverTime Request"

    state = fields.Selection([
        ('new','Draft'),
        ('m_a','Manager Approved'),
        ('wait','HOD Approved'),
        ('hr_approve','HR Approved'),
        ('done', 'Done'),
        ], string='Status', readonly=True, index=True, copy=False, default='new', track_visibility='onchange')
    
    
    def unlink(self):
        for leave in self:
            if leave.state in ('done','hr_approve'):
                raise UserError(_('You cannot delete an order form  which is not draft or cancelled. '))
     
            return super(Overtime_MenuForm, self).unlink()
        
        
    @api.model
    def create(self, vals):
        if 'code' not in vals or vals['code'] == False:
            sequence = self.env.ref('de_employee_overtime_request.code')
            vals['code'] = sequence.next_by_id()
        return super(Overtime_MenuForm, self).create(vals)
    
    def submit(self):
        self.write({'state':'m_a'}) 

        
    def draft(self):
        self.write({'state':'wait'})
        self.update({'dep_date':datetime.now().strftime('%Y-%m-%d'),'dept_approve_by':self.env.user}) 
    
    def wait(self):
        self.write({'state':'hr_approve'})
        self.update({'hod_date':datetime.now().strftime('%Y-%m-%d'),'hod_approve_by':self.env.user})
        
    def approve(self):
        self.write({'state':'done'})    
        
   
    code=fields.Char('Code',copy=False)
    name=fields.Many2one('hr.employee',string="Employee",required=True)
    start_date=fields.Date("Start Date",required=True)
    end_date=fields.Date("End Date",required=True)
    approve_date=fields.Date('Approve Date',readonly=True)
    hod_date=fields.Date('HOD Approved Date',readonly=True)
    dep_date=fields.Date('Department Approved Date',readonly=True)
    hod_approve_by=fields.Many2one('res.users','Hod Approved By',readonly=True)
    dept_approve_by=fields.Many2one('res.users','department Approved By',readonly=True)
    payroll=fields.Boolean('Include in Payroll',default=True)
    department=fields.Many2one(related='name.department_id')
    
    dept_manager=fields.Many2one(related='name.parent_id')
    number_hours=fields.Float("Number of Hours")
    company_id=fields.Many2one('res.company','Company',readonly=True,default=lambda self:self.env.company.id)

    note = fields.Text('Notes')
    
    
    @api.onchange('start_date','end_date')
    def compute_number_hours(self):
        for rec in self:
            employee_records = self.env['hr.attendance'].search([('employee_id', '=', rec.name.id)])
            avg_time = 0
            total_hours = 0
            if rec.name.resource_calendar_id.hours_per_day:
                avg_time = rec.name.resource_calendar_id.hours_per_day
            count = 0
            for employee_record in employee_records:
                if rec.start_date and rec.end_date:
                    if rec.start_date <= employee_record.check_in.date() and rec.end_date >= employee_record.check_in.date():
                        count = count + 1
                        delta = employee_record.check_out - employee_record.check_in
                        total_hours = (total_hours + delta.total_seconds() / 3600.0) - (avg_time)
            rec.number_hours = total_hours
            
            
    @api.constrains('number_hours')
    def hours_val(self):
        for s in self:
            if s.number_hours<=0 or s.number_hours<=0.00:
                raise Warning("You can't add less than zero Hours!") 
        
    
class hr_overtime_Form(models.Model):
    _inherit ='hr.payslip'
    
    def compute_sheet(self):
        
        other_inputs = self.env['hr.payslip.input.type'].search([('code','=', 'OVT')])
        overtime = self.env['employee.overtime'].search([('name','=', self.employee_id.id),('state','=', 'done'),('start_date','>=', self.date_from),('end_date','<=', self.date_to)])
        data = []
        for input in other_inputs:
            for hours in overtime:            
                data.append((0,0,{
                            'payslip_id': self.id,
                            'sequence': 1,
                            'code': input.code,
                            'contract_id': self.contract_id.id,
                            'input_type_id': input.id,
                            'amount': ((self.contract_id.wage/30)/8)*hours.number_hours,
                            }))
        self.input_line_ids = data
        liness = super(hr_overtime_Form, self).compute_sheet()
                        
        return liness
        