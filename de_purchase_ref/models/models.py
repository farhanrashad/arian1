# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMoveInherit(models.Model):
    _inherit = 'stock.move.line'

    def _move_sale_ref(self):
        picking = self.env['stock.picking'].search([('name','=',self.reference)])
        self.sale_ref = picking.sale_ref


    sale_ref = fields.Char(string="Sale Ref", compute='_move_sale_ref')
    categ_id = fields.Many2one(related='product_id.categ_id')
    category_id = fields.Many2one('product.category', string="Product Category")

    @api.onchange('product_id')
    def gettingd_category_id(self):
        self.category_id = self.categ_id


class MrpProductionInherit(models.Model):
    _inherit = 'mrp.production'
    
    categ_id = fields.Many2one(related='product_id.categ_id')
 
    category_id = fields.Many2one('product.category', string="Product Category")

    @api.onchange('product_id')
    def gettingd_category_id(self):
        self.category_id = self.categ_id
        
