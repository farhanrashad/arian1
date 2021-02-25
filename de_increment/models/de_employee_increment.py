from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import date


class EmployeeTab(models.Model):
    _inherit = 'hr.contract'

    increment_id = fields.One2many('hr.contract.increment', 'contract_id', string='increment')

    def employee_increment_action(self):
        print('auto-increment-call-------------  ')
        current_date_time = date.today()
        contract_ids = self.env['hr.contract'].search([])
        for contract in contract_ids:
            print('--------- contract name', contract.name)

            for rec in contract_ids.increment_id:

                inc_amount = rec.increment_amount
                print('incremnt info-------', inc_amount)
                eft_date = rec.increment_effective_date
                print('effective date-------', eft_date)

                if current_date_time == eft_date:
                    total_wage = self.wage + inc_amount
                    # print('wages info-------', self.wage)

                    print('total of wages-------', total_wage)

                    # self.wage = total_wage
                    # contract.write({'wage':total_wage})


class EmployeeIncrement(models.Model):
    _name = 'hr.contract.increment'
    _description = 'employee increment'

    years = fields.Selection(selection=
                             [('2021', '2021'), ('2022', '2022'), ('2023', '2023'),
                              ('2024', '2024'), ('2025', '2025')], string='Years', required=True)
    increment_amount = fields.Float(string='Amount', required=True)
    increment_effective_date = fields.Date(string='Increment Effective Date', required=True)
    contract_id = fields.Many2one('hr.contract')

    # @api.model
    # def create(self, vals):
    #     # if vals.get('name', _('New')) == _('New'):
    #     #     vals['name'] = self.env['ir.sequence'].next_by_code('employee.insurance.sequence')
    #
    #     if int(vals['increment_amount']) <= 0:
    #         raise UserError('Insurance amount must be greater than 0.')
    #
    #     result = super(EmployeeIncrement, self).create(vals)
    #     return result
