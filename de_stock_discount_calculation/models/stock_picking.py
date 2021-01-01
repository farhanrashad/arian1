# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    
    tax_before_id = fields.Many2one('account.tax', string='Tax Before Discount')
    after_tax_id = fields.Many2one('account.tax', string='Tax After Discount')
    discount = fields.Float(string='Discount %')
    is_before_tax = fields.Boolean(string='Before Tax')
    is_after_tax = fields.Boolean(string='After Tax')
    currency_id = fields.Many2one('res.currency', 'Currency')
    total_amount = fields.Float(string='Total', store=True, readonly=True, compute='_amount_all')
    amount_untaxed = fields.Float(string='Untaxed Amount', store=True, readonly=True, compute='_amount_all')
    amount_tax = fields.Float(string='Taxes', store=True, readonly=True, compute='_amount_all')
    
    
    
    @api.onchange('discount')
    def onchange_discount(self):
        for line in self.move_ids_without_package: 
            total =  (line.unit_price * line.product_uom_qty) + line.tax_amount
            discount_amount = total * (self.discount/100)
            line.update({
                'discount': self.discount,
                'subtotal': total - discount_amount
            })
            
        
    
    
    @api.depends('move_ids_without_package.subtotal')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.move_ids_without_package:
                amount_untaxed += line.subtotal
                amount_tax += line.tax_amount 
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'total_amount': amount_untaxed + amount_tax,
                })
            

    
    @api.onchange('tax_before_id')
    def onchange_tax_before_discount(self):
        if self.tax_before_id:
            self.is_before_tax = True
            for line in self.move_ids_without_package:
                line.update({
                        'tax_amount' : (self.tax_before_id.amount/100) *  (line.unit_price * line.product_uom_qty),
                        
                    })
        else:
            self.is_before_tax = False
            for line in self.move_ids_without_package:
                line.update({
                        'tax_amount' : (self.tax_before_id.amount/100) * (line.unit_price * line.product_uom_qty),
                        
                    }) 
        
        
        
    @api.onchange('after_tax_id')
    def onchange_tax_after_discount(self):
        if self.after_tax_id:
            self.is_after_tax = True
            if self.discount > 0:
                for line in self.move_ids_without_package:
                    total =  (line.unit_price * line.product_uom_qty)
                    discount_amount = total * (line.discount/100)
                    line.update({
                        'subtotal': total - discount_amount,
                    })
                    
                for line in self.move_ids_without_package:
                    line.update({
                        'tax_amount' : (self.after_tax_id.amount/100) * ( (line.unit_price * line.product_uom_qty)  - (line.unit_price * line.product_uom_qty)),                        
                    })    
            else:
                for line in self.move_ids_without_package:                 
                    line.update({
                        'tax_amount' : (self.after_tax_id.amount/100) * (line.unit_price * line.product_uom_qty),
                    })
        else:
            self.is_after_tax = False
            for line in self.move_ids_without_package:
                line.update({
                        'tax_amount' : (self.after_tax_id.amount/100) * (line.unit_price * line.product_uom_qty),
                    })
                
        
        
    
    


class StockMove(models.Model):
    _inherit = 'stock.move'
    
    
    unit_price = fields.Float(related='product_id.lst_price') 
    tax_amount = fields.Float(string='Tax Amount') 
    discount = fields.Float(string='Discount %')
    currency_id = fields.Many2one('res.currency', 'Currency')
    subtotal = fields.Float(string='Subtotal', compute='_compute_amount_subtotal') 
    
    
    @api.depends('subtotal','unit_price', 'product_uom_qty')    
    def _compute_amount_subtotal(self):
        for line in self:
            total =  (line.unit_price * line.product_uom_qty) + line.tax_amount
            discount_amount = total * (line.discount/100)
            line.update({
                'subtotal': total - discount_amount
            })
           