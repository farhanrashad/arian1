# -*- coding: utf-8 -*-
from odoo import models,fields,  _
# from odoo.exceptions import UserError


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
#             'confirm_by': self.env.user,
#             'confirm_date': datetime.today(),
        })
        
    def check_confirm_bank(self):
        self.write({
            'state': 'confirm',
#             'confirm_by': self.env.user,
#             'confirm_date': datetime.today(),
        })
        
        
        
        
        
        
        
    # , track_visibility = 'onchange'

    # def name_get(self):
    #     my_list = []
    #     for r in self:
    #         dataa = r.my_name
    #         if r.my_name:
    #             # dataa += " ({})".format(r.age)+" ({})".format(r.dob)
    #             my_list.append((r.id, dataa))
    #             # print(my_list,"\n")
    #     return my_list

