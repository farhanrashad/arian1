# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    _description = ''
    
    contact = fields.Char('Contact', compute='_compute_contact')
    
    
    def _compute_contact(self):
        for rec in self:
            stock_picking_obj = self.env['stock.picking'].search([('name', '=', rec.reference)])
            if stock_picking_obj:
                rec.contact = stock_picking_obj[0].name
            else:
                rec.contact = None
