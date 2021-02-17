# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime
import math
from collections import defaultdict

class de_sale_order(models.Model):
    _inherit = 'sale.order'


           
    product_tmpl_ids = fields.One2many('sale.order.total', 'order_id', )

    
        
    @api.onchange('order_line')
    def onchange_payment_term(self):
        for input in self.product_tmpl_ids:
            input.unlink()
        variants = []
        variant_name = ''
        for records in self.order_line:
            for record in records:
                variants_name = record.product_template_id.name
                if variants_name in variants or variants_name == False:
                    continue
                else:
                    variants.append(variants_name)

        variants_quantity = []
        variants_amount = []
        for i in variants:
            variants_quantity.append(0)
            variants_amount.append(0)
        variatns_total_quantities = dict(zip(variants, variants_quantity))
        variatns_total_amounts = dict(zip(variants, variants_amount))

        for records in self.order_line:
            for record in records:
                variants_name = record.product_template_id.name
                if variants_name in variatns_total_quantities and variants_name in variatns_total_amounts:
                    qty = variatns_total_quantities[variants_name]
                    qty = qty + record.product_uom_qty
                    variatns_total_quantities[variants_name] = qty
                    amnt = variatns_total_amounts[variants_name]
                    amnt = amnt + record.price_subtotal
                    variatns_total_amounts[variants_name] = amnt

        data = []
        for key in variants:
            data.append((0, 0, {
                'parent_product': key,
                'total_quantity': variatns_total_quantities[key],
                'total_amount': variatns_total_amounts[key],
            }))
        self.product_tmpl_ids = data
    





            
class SaleOrderTotal(models.Model):
    _name = 'sale.order.total'
    _description = 'sale order total quantity'


    
    parent_product = fields.Char(string="Parent Product")
    total_quantity = fields.Float(string="Total Quantity")
    total_amount = fields.Float(string="Total Amount")
    
    order_id = fields.Many2one('sale.order')