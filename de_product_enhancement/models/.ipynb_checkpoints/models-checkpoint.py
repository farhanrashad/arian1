# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    purchase_id = fields.Char(string='Customer PO Number', required=True)
#     delivery_date = fields.Date(string='Delivery Date', required=True)
    