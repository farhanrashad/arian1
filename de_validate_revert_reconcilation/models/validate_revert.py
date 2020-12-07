# -*- coding: utf-8 -*-
from odoo import models,fields,  _
# from odoo.exceptions import UserError


class AccountBandkStatementInherit(models.Model):
    _inherit = 'account.bank.statement'

    state = fields.Selection([
              ('sent_for_validation', 'Sent for Validation'),
              ])

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

