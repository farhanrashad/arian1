# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMoveInherit(models.Model):
    _inherit = 'stock.move.line'

    sale_ref = fields.Many2one('sale.order', string="Sale Ref")
    categ_id = fields.Many2one(related='product_id.categ_id', string="Product Category")
 

class MrpProductionInherit(models.Model):
    _inherit = 'mrp.production'
    
    categ_id = fields.Many2one(related='product_id.categ_id', string="Product Category")
 
    category_id = fields.Many2one('product.category', string="Sale Ref")

    
    @api.onchange('categ_id')
    def myfunc(self):
        self.category_change = self.categ_id
