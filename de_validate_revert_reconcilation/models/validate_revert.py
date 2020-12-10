# -*- coding: utf-8 -*-
from odoo import models,fields,  _
from odoo import exceptions
from odoo.exceptions import UserError, ValidationError

class AccountBandkStatementInherit(models.Model):
    _inherit = 'account.bank.statement'
    
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
                  
               
#     @api.multi
    def write(self, values):

            st=''
            sql = """ select state from account_bank_statement where id ='""" + str(self.id) + """' """
            self.env.cr.execute(sql)
            st = self.env.cr.fetchone()
            if str(st[0]) == 'open':
                res = super(AccountBandkStatementInherit, self).write(values)
                return res
                 
            else:  
                
                if not self.user_has_groups('de_validate_revert_reconcilation.revert_reconciliation_users'):
                    raise exceptions.ValidationError('You are not allowed to make any change here!')
                res = super(AccountBandkStatementInherit, self).write(values)
                return res
