# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ExtraIssuance(models.Model):

    _name = 'extra.issuance'
    _rec_name = 'sale_order'

    sale_order = fields.Many2one('sale.order', string='Sale Order')
    reason = fields.Char(string='Reason')
    articles_lines = fields.One2many('extra.issuance.article.line', 'relation_article')
    component_lines = fields.One2many('extra.issuance.component.line', 'relation_component')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('processed', 'Processed'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved')],
        readonly=True, index=True, copy=False, default='draft')

    def action_process(self):

        for mrec in self.articles_lines:
            record = self.env['mrp.bom'].search([('product_tmpl_id', '=', mrec.product_id.product_tmpl_id.id)])
            for rec in record:
                component_exists = self.env['extra.issuance.component.line'].search([('relation_component', '=', self.id)])
                if not component_exists:
                    self.env['extra.issuance.component.line'].create({
                        'relation_component': self.id,
                        'product_id': rec.bom_line_ids.product_id.id,
                        'component_qty': rec.bom_line_ids.product_qty * mrec.quantity,
                    })
                for component in component_exists:
                    if component.product_id.id == rec.bom_line_ids.product_id.id:
                        component.component_qty += rec.bom_line_ids.product_qty*mrec.quantity
                    else:
                        self.env['extra.issuance.component.line'].create({
                            'relation_component': self.id,
                            'product_id': rec.bom_line_ids.product_id.id,
                            'component_qty': rec.bom_line_ids.product_qty * mrec.quantity,
                        })
        self.write({'state': 'processed'})
    def action_submit(self):
        self.write({'state': 'submitted'})

    def action_approve(self):
        # self.write({'state': 'approved'})

        picking_delivery = self.env['stock.picking.type'].search([('code', '=', 'internal')], limit=1)
        print(picking_delivery.default_location_src_id.name)
        # picking_incoming = self.env['stock.picking.type'].search([('code', '=', 'incoming')], limit=1)
        # print(self.return_id.delivery_location)
        vals = {
            'location_id': picking_delivery.default_location_src_id.id,
            'location_dest_id': picking_delivery.default_location_dest_id.id,
            'partner_id': self.env.user.id,
            'picking_type_id': picking_delivery.id,
            'origin': self.sale_order.name,
        }
        picking = self.env['stock.picking'].create(vals)
        print('header created')
        for line in self.component_lines:
            lines = {
                'picking_id': picking.id,
                'product_id': line.product_id.id,
                'name': 'Internal Transfer',
                'product_uom': line.product_id.product_tmpl_id.uom_id.id,
                'location_id': picking_delivery.default_location_src_id.id,
                'location_dest_id': picking_delivery.default_location_dest_id.id,
                'product_uom_qty': line.component_qty,
                'quantity_done': line.component_qty,
            }
            stock_move = self.env['stock.move'].create(lines)
            print('lines created')
            moves = {
                'move_id': stock_move.id,
                'product_id': line.product_id.id,
                'location_id': picking_delivery.default_location_src_id.id,
                'location_dest_id': picking_delivery.default_location_dest_id.id,
                'product_uom_id': line.product_id.uom_id.id,
                'product_uom_qty': line.component_qty,
            }
            stock_move_line_id = self.env['stock.move.line'].create(moves)
            print('moves created')

class ExtraIssuanceArticleLine(models.Model):

    _name = 'extra.issuance.article.line'

    relation_article = fields.Many2one('extra.issuance')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity')

class ExtraIssuanceComponentLine(models.Model):

    _name = 'extra.issuance.component.line'

    relation_component = fields.Many2one('extra.issuance')
    product_id = fields.Many2one('product.product', string='Component')
    component_qty = fields.Float(string='Total Quantity')
