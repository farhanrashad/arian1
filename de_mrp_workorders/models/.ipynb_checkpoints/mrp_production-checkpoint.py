# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from odoo import exceptions
from odoo.exceptions import UserError, ValidationError


# class MrpProduction(models.Model):
#     _inherit = 'mrp.production'
    
    
#     def _prepare_wc_analytic_line(self, wc_line):
#         wc = wc_line.workcenter_id
#         hours = wc_line.duration / 60.0
#         value = hours * wc.costs_hour
#         account = wc.costs_hour_account_id.id
#         return {
#             'name': wc_line.name + ' (H)',
#             'amount': -value,
#             'account_id': account,
#             'ref': wc.code,
#             'unit_amount': hours,
#             'company_id': self.company_id.id,
#         }

#     def _costs_generate(self):
#         """ Calculates total costs at the end of the production.
#         """
#         self.ensure_one()
#         AccountAnalyticLine = self.env['account.analytic.line'].sudo()
#         for wc_line in self.workorder_ids.filtered('workcenter_id.costs_hour_account_id'):
#             vals = self._prepare_wc_analytic_line(wc_line)
#             precision_rounding = wc_line.workcenter_id.costs_hour_account_id.currency_id.rounding
#             if not float_is_zero(vals.get('amount', 0.0), precision_rounding=precision_rounding):
#                 # we use SUPERUSER_ID as we do not guarantee an mrp user
#                 # has access to account analytic lines but still should be
#                 # able to produce orders
#                 AccountAnalyticLine.create(vals)

#     def button_mark_done(self):
#         self.ensure_one()
#         res = super(MrpProduction, self).button_mark_done()
#         self._costs_generate()
#         return res

    
 