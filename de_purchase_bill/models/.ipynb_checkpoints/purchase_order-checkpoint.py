# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    

    def action_create_bill(self): 
        pass
    
    
    
    
class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'    
    
    is_downpayment = fields.Boolean(
        string="Is a down payment", help="Down payments are made when creating invoices from a Purchase order."
        " They are not copied when duplicating a Purchase order.")