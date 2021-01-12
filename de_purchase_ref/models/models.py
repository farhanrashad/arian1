# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, datetime, timedelta
import dateutil.parser
from odoo.exceptions import UserError

class StockMoveInherit(models.Model):
    _inherit = 'stock.move.line'
    
    def _move_sale_ref(self):
        picking = self.env['stock.picking'].search([('name','=',self.reference)])
        self.sale_ref = picking.sale_ref
    
    sale_id = fields.Char(string="Sale Reference")
    categ_id = fields.Many2one(related='product_id.categ_id')
    category_id = fields.Many2one('product.category', string="Product Category")

    @api.onchange('product_id')
    def gettingd_category_id(self):
        self.category_id = self.categ_id

class MrpProductionInherit(models.Model):
    _inherit = 'mrp.production'
    
    categ_id = fields.Many2one(related='product_id.categ_id')
 
    category_id = fields.Many2one('product.category', string="Product Category t")

    @api.onchange('product_id')
    def gettingd_category_id(self):
        self.category_id = self.categ_id
        
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    
    def calculate_date(self):    
        specific_date = self.commitment_date
        new_due_date = specific_date+ timedelta(days = self.insert_days) 
        new_date = datetime.strptime(str(new_due_date),'%Y-%m-%d %H:%M:%S')
        new_date = new_date.date()
        new_date=str(new_date)
#         raise UserError((type(self.bl_date)))
        self.bl_date = new_date
                
    insert_days = fields.Integer(string="Expected On Boarding Date after Delivery Date")
    days_days = fields.Char(default=' ',readonly=True)
    
    bl_date = fields.Char(string="BL Date", readonly=True, compute='calculate_date')
    
    


#  compute='calculate_date'
