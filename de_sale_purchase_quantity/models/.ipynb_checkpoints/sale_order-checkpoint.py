# -*- coding: utf-8 -*-
import math
from collections import defaultdict

from odoo import models, fields, api, _

class SaleOrderExt(models.Model):
    _inherit = 'sale.order'

    total_quantity = fields.Float(string="Total Quantity", compute='cal_total_quantity')
    total_delivered_quantity = fields.Float(string="Total Delivered Quantity", compute='cal_total_quantity')
    total_invoiced_quantity = fields.Float(string="Total Invoiced Quantity", compute='cal_total_quantity')


    def cal_total_quantity (self):
        quantity=0
        delivered=0
        invoiced=0
        for record in self:
            for rec in record.order_line:
                quantity=quantity+rec.product_uom_qty
                delivered=delivered+rec.qty_delivered
                invoiced=invoiced+rec.qty_invoiced
        self.total_quantity=quantity
        self.total_delivered_quantity=delivered
        self.total_invoiced_quantity=invoiced
        # self.total_delivered_quantity = 55


