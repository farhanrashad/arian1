# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class stockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('waiting', 'Waiting Another Operation'),
            ('confirmed', 'Waiting'),
            ('assigned', 'Partially Available'),
            ('partially_available', 'Ready'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ],
    )
    
    
    def action_assign(self):
        res = super(stockPickingInherit, self).action_assign()
        move_count = 0
        picking_move_count = 0
        for line in self.move_ids_without_package: 
            move_count = move_count + 1
            
        for move_line in self.move_ids_without_package: 
            if move_line.state == 'assigned':
                picking_move_count = picking_move_count + 1    
        
        if picking_move_count != move_count:        
            self.show_validate = True
        
        if picking_move_count == move_count:
            self.show_validate = False
            self.update({
                'state': 'partially_available',
                })    
               
        return res
 
    def button_validate(self):        
        origins = self.env['stock.picking'].search([('origin','=',self.name),('state','=', 'done')])
        for picking_line in  self.move_ids_without_package:            
            bom = self.env['mrp.bom'].search([('product_id','=',picking_line.product_id.id)])
            for bom_line in bom.bom_line_ids:                    
                for document in origins:
                    for doc_line in document.move_ids_without_package:
                        if doc_line.product_id.id == bom_line.product_id.id:
                            if picking_line.product_uom_qty <= doc_line.quantity_done: 
                                pass
                            else:
                                raise UserError(('You can only reserved quantity '+ doc_line.quantity_done + ' for product ' + picking_line.product_id.name))

        
        res = super(stockPickingInherit, self).button_validate()
        
        return res


