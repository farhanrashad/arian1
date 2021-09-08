from odoo import models,fields, api, _

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'
#     _order = 'departments_id asc'
    
    departments_id = fields.Many2one(related='employee_id.department_id', string="Department Name", store=True)
    barcode = fields.Char(related='employee_id.barcode', string="Batch ID", store=True)
#     department_id = fields.Many2one('hr.department', stzzring="Department", store=True)
#     emp_code = fields.Char(string="Seq", compute='_get_employee_sequence_no', store=True)
    
#     @api.depends('employee_id')
#     def _get_employee_sequence_no(self):
#         employees = self.env['hr.employee'].search([])
#         for rec in employees:
#             if rec.sequence_no:
#                 rec.update({
#                     'emp_code': rec.sequence_no,
#                 })
                