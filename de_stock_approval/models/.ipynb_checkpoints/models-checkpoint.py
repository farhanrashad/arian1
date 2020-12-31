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
            ('partially_available', 'Partially Available'),
            ('assigned', 'Ready'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ],
    )
    
    
    def action_assign(self):
        res = super(stockPickingInherit, self).action_assign()

        for rec in self.move_ids_without_package :           
            if rec.state != 'assigned':
                self.update({
                    'state': 'partially_available',
                    'show_check_availability' :  True
                })
                
                break
            else: 
                self.update({
                    'state': 'assigned'
                })
                
        for rec in self.move_ids_without_package :           
            self.update({
                    'show_check_availability' :  True
                })
            
        if self.state == 'partially_available':
            self.show_check_availability = True
        return res
 