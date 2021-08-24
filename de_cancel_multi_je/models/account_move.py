# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError



class AccountMove(models.Model):
    _inherit = 'account.move'
    _description = 'Inherit Account Move to Cancel Multiple at a time.'
    
    
    def entry_mark_as_cancel_action(self):
        for id in self.ids:
            move_rec = self.browse(id)
            move_rec.button_draft()
            move_rec.button_cancel()