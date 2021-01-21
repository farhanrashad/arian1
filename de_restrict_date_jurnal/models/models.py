# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime, timedelta
from odoo.exceptions import UserError 




class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

#     invoice_date = fields.Date()
    
    @api.constrains('invoice_date')
    def future_date_restriction(self):
        today = date.today()
        if self.type == 'out_invoice': 
            if self.invoice_date:
                if self.invoice_date > today:
                    raise UserError("Sorry! You can't select future invoice_date ")
        if self.date:
            if self.date > today:
                raise UserError("Sorry! You can't select future Accounting date ")
        

            
            