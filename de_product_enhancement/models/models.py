# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from odoo import exceptions
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class StockQuant(models.Model):
    _inherit = 'stock.quant'
    
    @api.model
    def create(self, values):
        t_uid = self.env.uid
        if self.user_has_groups('de_product_enhancement.group_stock_quant_restrict'):
            raise exceptions.ValidationError('You are not allowed to create Stock')    
        res = super(StockQuant, self).create(values)
        return res
    
    
#     @api.multi
    def write(self, values):
        t_uid = self.env.uid
        if self.user_has_groups('de_product_enhancement.group_stock_quant_restrict'):
            raise exceptions.ValidationError('You are not allowed to update Stock')
           
        res = super(StockQuant, self).write(values)
        return res

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    def action_done(self):
        res = super(StockPicking, self).action_done()
        if self.state != 'done':
            self.update({
                'state': 'done'
            })
      
        return res



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    bill_amount = fields.Float(string="Amount Billed", compute='_compute_bill_amount', store=True)
    remaining_bill_amount = fields.Float(string="Remaining Amount to bill", compute='_compute_bill_amount', store=True)

    @api.onchange('amount_total')
    def onchange_amount_total(self):
        for order in self:
            sum_invoice_amount = 0
            for line in order.order_line:
                sum_invoice_amount = sum_invoice_amount + (line.qty_invoiced * line.price_unit)
            order.bill_amount = sum_invoice_amount
            order.remaining_bill_amount = order.amount_total - sum_invoice_amount
            
    @api.depends('amount_total','order_line')
    def _compute_bill_amount(self):
        for order in self:
            sum_invoice_amount = 0
            for line in order.order_line:
                sum_invoice_amount = sum_invoice_amount + (line.qty_invoiced * line.price_unit)
            order.bill_amount = sum_invoice_amount
            order.remaining_bill_amount = order.amount_total - sum_invoice_amount

    

    def button_done(self):
        res = super(PurchaseOrder, self).button_done()
        picking = self.env['stock.picking'].search([('origin','=',self.name)])
        for pick in picking:
            if pick.state != 'done':
                pick.update({
                    'state': 'cancel'
                })
      
        return res     
    
    receipt_date = fields.Date(string='Receipt Date')
    payment_term_date =  fields.Date(string='Expected Payment Date')
    is_received = fields.Boolean(string="Is Received")
    
    @api.onchange('receipt_date','payment_term_id')
    def _check_change(self):
        current_date = date.today()
        if self.receipt_date:
            date_1= (datetime.strptime(str(self.receipt_date), '%Y-%m-%d')+relativedelta(days =+ self.payment_term_id.line_ids.days))
            self.payment_term_date =date_1
        else:    
            date_2= (datetime.strptime(str(current_date), '%Y-%m-%d')+relativedelta(days =+ self.payment_term_id.line_ids.days))
            self.payment_term_date =date_2
    
    @api.onchange('receipt_date')
    def onchange_receipt_date(self):
        if self.receipt_date:
            self.date_planned = self.receipt_date


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    purchase_id = fields.Char(string='Customer PO Number', required=True)

    
class ProductTemplate(models.Model):
    _inherit = 'product.template'



    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        # TDE FIXME: should probably be copy_data
        self.ensure_one()
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)") % self.name
            default['seller_ids'] = self.seller_ids
        return super(ProductTemplate, self).copy(default=default)
        

    @api.model
    def create(self, values):
        res = super(ProductTemplate, self).create(values)
        try:
            if values['purchase_ok'] == True:
                if values['seller_ids']:
                    pass
        except:
            raise exceptions.ValidationError('Please Select Vendor On Purchase Tab.')    
        
        return res
    
    allow_location = fields.Boolean(string="Is Finished or Un-Finished") 

    @api.onchange('allow_location')
    def onchange_location(self):
        if self.allow_location == True:
            if self.property_stock_production.id == 15:
                self.property_stock_production = 22
        elif self.allow_location == False:        
            if self.property_stock_production.id == 22:
                self.property_stock_production = 15    
       