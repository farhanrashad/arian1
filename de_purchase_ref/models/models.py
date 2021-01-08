# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMoveInherit(models.Model):
    _inherit = 'stock.move.line'

    sale_ref = fields.Many2one('sale.order', string="Sale Ref")
    categ_id = fields.Many2one(related='product_id.categ_id')
    category_id = fields.Many2one('product.category', string="Product Category")

    @api.onchange('categ_id')
    def gettingd_category_id(self):
        self.category_id = self.categ_id


class MrpProductionInherit(models.Model):
    _inherit = 'mrp.production'
    
    categ_id = fields.Many2one(related='product_id.categ_id')
 
    category_id = fields.Many2one('product.category', string="Product Category")

    @api.onchange('categ_id')
    def gettingd_category_id(self):
        self.category_id = self.categ_id

        
