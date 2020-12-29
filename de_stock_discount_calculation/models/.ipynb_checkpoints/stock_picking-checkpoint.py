# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    
    tax_before_discount = fields.Many2one('account.tax', string='Tax Before Discount')
    tax_after_discount = fields.Many2one('account.tax', string='Tax After Discount')
    discount = fields.Float(string='Discount %')
    
    


class StockMove(models.Model):
    _inherit = 'stock.move'
    
    
    unit_price = fields.Float(related='product_id.lst_price') 
    tax_calculation = fields.Float(string='Tax Amount') 
    subtotal = fields.Float(string='Subtotal') 