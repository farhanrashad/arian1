# -*- coding: utf-8 -*-
import math
from collections import defaultdict

from odoo import models, fields, api, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    total_quantity = fields.Float(string="Total Demand Qty", compute='cal_total_quantity')
    total_received_quantity = fields.Float(string="Total Received Qty", compute='cal_total_quantity')
    total_billed_quantity = fields.Float(string="Total Invoiced Qty", compute='cal_total_quantity')


    def cal_total_quantity (self):
        quantity=0
        received=0
        invoiced=0
        for purchase_order in self:
            for order_line in purchase_order.order_line:
                quantity=quantity+order_line.product_qty
                received=received+order_line.qty_received
                invoiced=invoiced+order_line.qty_invoiced
        self.total_quantity=quantity
        self.total_received_quantity=received
        self.total_billed_quantity=invoiced


