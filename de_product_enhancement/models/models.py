# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from datetime import datetime

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
    
    allow_location = fields.Boolean(string="Change Location")    