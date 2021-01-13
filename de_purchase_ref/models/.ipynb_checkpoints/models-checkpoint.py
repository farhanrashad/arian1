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
        self.bl_date = new_date
                
    insert_days = fields.Integer(string="Expected On Boarding Date after Delivery Date")
    days_days = fields.Char(default=' ',readonly=True)
    
    bl_date = fields.Date(string="BL Date",compute='calculate_date')
       
class AccountPaymentTermLineInherit(models.Model):
    _inherit = "account.payment.term.line"
    
    option = fields.Selection([
            ('day_after_bl_date', "days after the BL date"),
            ('day_after_invoice_date', "days after the invoice date"),
            ('after_invoice_month', "days after the end of the invoice month"),
            ('day_following_month', "of the following month"),
            ('day_current_month', "of the current month"),
        ],
        default='day_after_invoice_date', required=True, string='Options'
        )


class accountMoveInherit(models.Model):
    _inherit = 'account.move'

    
    @api.model
    def create(self, values):
        rec = super(accountMoveInherit, self).create(values)
        payment_term = self.env['account.payment.term'].search([('id' ,'=',rec.invoice_payment_term_id.id)])
        select_by_date = payment_term.line_ids.option
        select_by_day = payment_term.line_ids.days
        if select_by_date == 'day_after_bl_date':
            sale_id = self.env['sale.order'].search([('name','=',rec.invoice_origin)])
            bl_date = sale_id.bl_date
            new_due_date = bl_date + timedelta(days = select_by_day)
            rec.invoice_date_due = new_due_date
            print('------------inv dateee-----,',rec.invoice_date_due)
        return rec
    
    