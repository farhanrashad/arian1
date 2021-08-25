# -*- coding: utf-8 -*-

from odoo import models, api, _
from odoo.exceptions import UserError

class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'
    
    @api.model
    def render_qweb_pdf(self, res_ids=None, data=None):
        if self.model == 'account.move' and any(not m.is_invoice(include_receipts=True) for m in self.env[self.model].browse(res_ids)):
            pass
        return super(IrActionsReport, self).render_qweb_pdf(res_ids, data)