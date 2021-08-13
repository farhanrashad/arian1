# -*- coding: utf-8 -*-

from odoo import models, fields, api


class de_hr_attendance_report(models.Model):
    _inherit = 'hr.attendance'

    attendance_date = fields.Date(string="Attendance Date", compute='_compute_attendance_date', store=True)

    @api.depends('check_in')
    def _compute_attendance_date(self):
        for line in self:
            line.update({
                'attendance_date': line.check_in,
            })