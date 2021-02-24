# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    
    def button_validate(self):
      
        res = super(StockPicking, self).button_validate()
        if self.picking_type_id.name == 'Receipts':
            picking_delivery = self.env['stock.picking.type'].search([('name', '=', 'Quality at Reception')], limit=1)
            vals = {
                'location_id': picking_delivery.default_location_src_id.id,
                'location_dest_id': picking_delivery.default_location_dest_id.id,
                'picking_type_id': picking_delivery.id,
                'origin': self.origin,
                'state': 'assigned',
                'sale_ref': self.sale_ref,
            }
            picking = self.env['stock.picking'].create(vals)
            for line in self.move_ids_without_package:
                lines = {
                    'picking_id': picking.id,
                    'product_id': line.product_id.id,
                    'name': 'Quality at Reception',
                    'state': 'confirmed',
                    'product_uom': line.product_id.product_tmpl_id.uom_id.id,
                    'location_id': picking_delivery.default_location_src_id.id,
                    'location_dest_id': picking_delivery.default_location_dest_id.id,
                    'quantity_done': line.quantity_done,
                }
                stock_move = self.env['stock.move'].create(lines)
                
        if self.picking_type_id.name == 'Quality at Reception':
            picking_delivery = self.env['stock.picking.type'].search([('name', '=', 'Store Receiving')], limit=1)
            vals = {
                'location_id': picking_delivery.default_location_src_id.id,
                'location_dest_id': picking_delivery.default_location_dest_id.id,
                'picking_type_id': picking_delivery.id,
                'origin': self.origin,
                'state': 'assigned',
                'sale_ref': self.sale_ref,
            }
            picking = self.env['stock.picking'].create(vals)
            for line in self.move_ids_without_package:
                lines = {
                    'picking_id': picking.id,
                    'product_id': line.product_id.id,
                    'name': 'Quality at Reception',
                    'state': 'confirmed',
                    'product_uom': line.product_id.product_tmpl_id.uom_id.id,
                    'location_id': picking_delivery.default_location_src_id.id,
                    'location_dest_id': picking_delivery.default_location_dest_id.id,
                    'quantity_done': line.quantity_done,
                }
                stock_move = self.env['stock.move'].create(lines)        
                

        
        return res

