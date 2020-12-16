# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from odoo import exceptions 
from odoo.exceptions import UserError, ValidationError 

class HrEmployee(models.Model):
    _inherit = 'hr.department'
    
    allow_overtime = fields.Boolean(string="Allow Overtime", store=True)

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'
    
    @api.model
    def cron_create_overtime(self):
        if self.employee_id.allow_overtime == True:
            vals = {
                'name': self.employee_id.id,
                'date':  self.check_in,
                'check_in': self.check_in,
                'check_out': self.check_in,
                'total_hours': self.worked_hours,
                'overtime_hours': self.worked_hours - self.employee_id.resource_calendar_id.hours_per_day,
                      }
            overtime_lines = env['hr.employee.overtime'].create(vals) 
    
class HrEmployee(models.Model):
    _inherit = 'hr.employee'
     
    allow_overtime = fields.Boolean(related='department_id.allow_overtime', store=True)
    
    
class EmployeeOvertime(models.Model):
    _name = 'hr.employee.overtime'
    _description = 'Employee Overtime'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    
    def unlink(self):
        for leave in self:
            if leave.state in ('to_approve','approved','paid'):
                raise UserError(_('You cannot delete an order form  which is not draft or close. '))
     
            return super(EmployeeAdvanceSalary, self).unlink()
        
    def action_approve(self):
        overtime_rule = self.env['hr.employee.overtime.rule'].search([('employee_ids','=', self.name.id)])
        for rule in overtime_rule:
            if rule.overtime_hours < self.overtime_hours:
                raise UserError(_('Overtime exceeded for the internal.'))
            else:                
                self.write ({
                        'state': 'approved'
                    })
        
    def action_confirm(self):
        self.write ({
                'state': 'to_approve'
            })    
        
    def action_refuse(self):
        self.write ({
                'state': 'refused'
            })
        
    def action_draft(self):
        self.write ({
                'state': 'draft'
            })    
    
    name = fields.Many2one('hr.employee', string="Employee", store=True)
    date = fields.Date(string='Date', required=True)
    check_in = fields.Datetime(string="Check In", readonly=True)
    check_out = fields.Datetime(string="Check Out", readonly=True)
    total_hours = fields.Float(string="Total Hours", readonly=True)
    overtime_hours = fields.Float(string="Overtime Hours", readonly=True)
    state = fields.Selection([
        ('draft', 'To Submit'),
        ('to_approve', 'To Approve'),
        ('refused', 'Refused'),
        ('approved', 'Approved'),        
        ('paid', 'Paid'),
        ('close', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    
    @api.onchange('date')
    def onchange_date(self):
        for rec in self:
            avg_time = 0 
            total_hours = 0
            if rec.name.resource_calendar_id.hours_per_day:
                avg_time = rec.name.resource_calendar_id.hours_per_day
            if rec.date:
                rec.check_in = None
                rec.check_out = None
                rec.overtime_hours = 0
                rec.total_hours = 0
            employee_records = self.env['hr.attendance'].search([('employee_id', '=', rec.name.id)])
            for employee_record in employee_records:
                
                if rec.date == employee_record.check_in.date():
                    rec.check_in = employee_record.check_in
                    rec.check_out = employee_record.check_out
                    
                    delta = rec.check_out - rec.check_in
                    total_hours = total_hours + delta.total_seconds() / 3600.0
            
            if total_hours - avg_time <= 0:
                rec.overtime_hours = 0
            else: 
                rec.overtime_hours = total_hours - (avg_time)
            rec.total_hours = total_hours
    

    
class EmployeeOvertimeRule(models.Model):
    _name = 'hr.employee.overtime.rule'
    _description = 'Employee Overtime Rule'
    _rec_name = 'overtime_type_id'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    

    department_id = fields.Many2one('hr.department', string="Department", store=True)
    overtime_type_id = fields.Many2one('hr.employee.overtime.type', string="Overtime Type", store=True)
    employee_ids = fields.Many2many('hr.employee', string="Employee", store=True)
    date_from = fields.Date(string='Date From', required=True)
    date_to = fields.Date(string="Date To")
    overtime_hours = fields.Integer(string="Allow Overtime Hours", required=True)
    type = fields.Selection(selection=[
            ('weekly', 'Weekly'),
            ('monthly', 'Monthly'),
            ('yearly', 'Yearly'),
        ], string='Type', required=True, store=True, index=True,tracking=True,
        default="yearly")
    overtime_type = fields.Selection(selection=[
            ('fixed', 'Fixed'),
            ('percent', 'Percentage'),
        ], string='Overtime Type', required=True, store=True, index=True,  tracking=True,
        default="fixed")
    overtime_amount = fields.Float(string="Overtime Amount")
    
    
class EmployeeOvertimeRule(models.Model):
    _name = 'hr.employee.overtime.type'
    _description = 'Employee Overtime Type'

    name = fields.Char(string="Name", store=True)    

