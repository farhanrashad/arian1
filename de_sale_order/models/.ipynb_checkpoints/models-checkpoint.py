# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime

class de_sale_order(models.Model):
    _inherit = 'sale.order'
       
#     raise UserError(('count'))

    sale_order_total_chile_id = fields.One2many('sale.order.total', 'sale_order_parent_id', string="Total Qty Amount")
    

#     fld = fields.Integer()
    @api.model
    def default_get(self,fields):
        rec = super(de_sale_order, self).default_get(fields)

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
        
        
        for key in variants:
            
            vals = {
                'parent_product': key,
                'total_quantity': variatns_total_quantities[key],
                'total_amount': variatns_total_amounts[key],
            }
            self.env['sale.order.total'].create(vals) 
#         rc = self.env['sale.order.total'].search([]) 
#         i = 0
#         for r in rc:
#             i = i + 1
#             if i == 2:
#                 raise UserError((r.parent_product," = ",r.total_quantity))
            
            
#         raise UserError((str(variatns_total_amounts)))
                    
#                 raise UserError((record.product_uom_qty))
#                 raise UserError((record.price_subtotal))
#         

#         z = {'a':1, 'b':2}
#         k = z['a']
#         k = k+1
#         z['a'] = k
#         raise UserError((str(z)))
        
        return rec
        
#     raise UserError((self.id))
#     parent_product = fields.Many2one('',string="Parent Product")
#     total_quantity = fields.Float(string="Total Quantity")
#     total_quantity = fields.Float(string="Total Quantity")
    
    

class SaleOrderTotal(models.Model):
    _name = 'sale.order.total'
    _description = 'sale order total quantity'
    
    parent_product = fields.Char(string="Parent Product")
    total_quantity = fields.Float(string="Total Quantity")
    total_amount = fields.Float(string="Total Amount")
    
    sale_order_parent_id = fields.Many2one('sale.order')

    def fn(self):
        raise UserError(('yes u are clicking me'))
    
    
#     Name of parent product
#     total sum of quantities for its variants
#     Total amount for its variants
        
        
#     def fn(self):
#         model = self.env.context.get('active_model')
#         rec = self.env[model].browse(self.env.context.get('active_id'))
        
#         rec.requested_model = self.assign_fleet.id
#         rec.state ='assigned'
#         rec.assign_by = self.env.user
#         rec.assign_date = datetime.today()
#         rec.image_fleet_request = self.assign_fleet.image_128
    
    
# record = model.browse(env.context['active_id'])
# count = 0
# for line in record.order_line:
#   count = count + 1
#   line.update({
#     'item_quote': count
#     })


