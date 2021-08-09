# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, datetime, timedelta
import dateutil.parser
from odoo.exceptions import UserError

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    @api.constrains('invoice_date')
    def future_invoice_date_restriction(self):
        today = date.today()
        if self.type == 'out_invoice':
            if self.invoice_date:
                if self.invoice_date > today:
                    raise UserError("Sorry! You can't select future Invoice Date! ")
                else:
                    if not self.user_has_groups('de_restrict_date_jurnal.group_back_date_allow_users'):
                        past_date = today - timedelta(days = 3)
                        if self.invoice_date < past_date:
                            raise UserError("Sorry, you are not allowed to post Bills/Invoices/JVs in dates prior to " + str(past_date) + "!")

    @api.constrains('date')
    def future_invoice_date_restriction(self): 
        for line in self:
            today = date.today()
            if line.date:
                if line.date > today:
                    raise UserError("Sorry! You can't select future Accounting Date!")
                else:
                    if not line.user_has_groups('de_restrict_date_jurnal.group_back_date_allow_users'): 
                        past_date = today - timedelta(days = 3)
                        if line.date < past_date:
                            raise UserError("Sorry, you are not allowed to post Bills/Invoices/JVs in dates prior to " + str(past_date))
                  
                    