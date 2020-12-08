# -*- coding: utf-8 -*-
from odoo import models,fields,  _
# from odoo.exceptions import UserError


class AccountBandkStatementInherit(models.Model):
    _inherit = 'account.bank.statement'
    
    
    #     @api.multi
#     def write(self, values):
#         t_uid = self.env.uid
#         if self.user_has_groups('de_validate_revert_reconcilation.revert_reconciliation_users'):
            
# #             raise exceptions.ValidationError('You are not allowed to update Stock')
           
#         res = super(AccountBandkStatementInherit, self).write(values)
#         return res
    

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
        