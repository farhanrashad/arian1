# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class stockPickingInherit(models.Model):
    _inherit = 'stock.picking'
    


    def action_assign(self):
        record = self.move_line_ids_without_package
        
        for rec in record:            
            if rec.state != 'assigned':
                self.update({
                    'state': 'partially_available'
                })
                break
            else: 
                self.update({
                    'state': 'assigned'
                })
        
                

    
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('waiting', 'Waiting Another Operation'),
            ('confirmed', 'Waiting'),
            ('partially_available', 'Partially Available'),
            ('assigned', 'Ready'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ],
    )