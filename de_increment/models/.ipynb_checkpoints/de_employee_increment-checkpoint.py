from odoo import api, fields, models
from odoo.exceptions import UserError
from datetime import date


class EmployeeTab(models.Model):
    _inherit = 'hr.contract'

    increment_id = fields.One2many('hr.contract.increment', 'contract_id', string='increment')

    def employee_increment_action(self):
        current_date = date.today()
        contract_ids = self.env['hr.contract'].search([('state', '=', 'open')])
        for contract in contract_ids:
            if contract.increment_id:
                for rec in contract.increment_id:
                    if rec.is_increment_applied == False:
                        if rec.increment_effective_date == current_date:
                            total_wage = contract.wage + rec.increment_amount
                            contract.wage = total_wage
                            rec.is_increment_applied = True
                            print('total of wages-------', contract.wage)


class EmployeeIncrement(models.Model):
    _name = 'hr.contract.increment'
    _description = 'employee increment'

    years = fields.Selection(selection=
                             [('2021', '2021'), ('2022', '2022'), ('2023', '2023'),
                              ('2024', '2024'), ('2025', '2025')], string='Years')
    increment_amount = fields.Float(string='Amount', required=True)
    increment_effective_date = fields.Date(string='Increment Effective Date', required=True)
    contract_id = fields.Many2one('hr.contract')
    is_increment_applied = fields.Boolean(default=False, readonly=True)
    description = fields.Char(string="Description")
    
    
    def unlink(self):
        if self.is_increment_applied == True:
            raise UserError(('Deletion is not allowed, Incase of increment is applied!'))
        return super(EmployeeIncrement,self).unlink()
    
    
    @api.constrains('increment_amount')
    def check_amount(self):
        if self.increment_amount <= 0:
            raise UserError(('Increment amount must be greater than 0.'))
    
    
    
    
    
    
