from odoo import models,fields, api, _

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'
#     _order = 'departments_id asc'
    
    departments_id = fields.Many2one(related='employee_id.department_id', string="Department Name", store=True)
    barcode = fields.Char(related='employee_id.barcode', string="Batch ID", store=True)
#     department_id = fields.Many2one('hr.department', stzzring="Department", store=True)
#     department_name = fields.Char(string="Department", compute='_get_employee_department', store=True)
    
#     @api.depends('employee_id')
#     def _get_employee_department(self):
#         for rec in self:
#             if rec.employee_id.department_id:
#                 rec.update({
#                     'department_name': rec.employee_id.department_id.name,
#                 })
                