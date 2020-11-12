# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    receipt_date = fields.Date(string='Receipt Date')
    
    @api.onchange('receipt_date')
    def onchange_receipt_date(self):
        if self.receipt_date:
            self.date_planned = self.receipt_date


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    purchase_id = fields.Char(string='Customer PO Number', required=True)
#     delivery_date = fields.Date(string='Delivery Date', required=True)
    