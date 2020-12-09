# -*- coding: utf-8 -*-
from odoo import models,fields,  _

class AccountBandkStatementInherit(models.Model):
    _inherit = 'account.bank.statement'
    

    is_access_revert = fields.Boolean('Access Reverst')
    state = fields.Selection(selection_add=[
              ('sent_for_validation', 'Sent for Validation'),
              ('confirm', 'Validated'),
              ])

    def action_Send_validation(self):
        self.write({
            'state': 'sent_for_validation',
        })
        
    def check_confirm_bank(self):
        self.write({
            'state': 'confirm',
        })
        
        