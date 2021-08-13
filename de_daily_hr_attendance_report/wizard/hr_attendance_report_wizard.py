# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class HrAttendanceReportWizard(models.TransientModel):
    _name = 'hr.attendance.report.wizard'
    _description = 'Daily Attendance Report'

    on_date = fields.Date(string='Date', required=True)
#     stop_at = fields.Date(string="To Date", required=True)
#     shop_ids = fields.Many2many('pos.multi.shop', string="Shop", required=True)

    def print_hr_attendance_report_xls(self):
#         if self.start_at > self.stop_at:
#             raise ValidationError(_('Invalid date !'))
        data = {
            'on_date': self.on_date,
#             'stop_at': self.stop_at,
#             'shop_ids': self.shop_ids.ids,
        }
        return self.env.ref('de_daily_hr_attendance_report.hr_attendance_report_xlsx').report_action(self, data=data)
