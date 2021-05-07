# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class StockQuant(models.Model):
    _inherit = 'stock.quant'
    _description = ''
    
    categ_id = fields.Many2one('product.category',string='Product Category',related='product_id.categ_id', store=True)
    