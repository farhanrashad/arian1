# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError



class AccountMoveLine (models.Model):
    _inherit = 'account.move.line'
    
    corresponding_account = fields.Many2one('account.account', string='Corresponding Account', compute='compute_corresponding_account')
    total = fields.Float(string='Total', compute='compute_debit_credit')
     
    def compute_corresponding_account(self):
        for rec in self:
            ids = []
            similar_ids = []
             
            if rec.move_id.line_ids:
                for line in rec.move_id.line_ids:
                    if line.account_id.id != rec.account_id.id:
                        ids.append(line.id)
                    else:
                        similar_ids.append(line.id)
                        
                if ids:
                    move_line = self.env['account.move.line'].search([('id','in',ids)], order="total desc", limit=1)
                else:
                    move_line = self.env['account.move.line'].search([('id','in',similar_ids)], order="total desc", limit=1)

                    
                
                if move_line:
                    rec.corresponding_account = move_line.account_id.id
                        
    def compute_debit_credit(self):
        for rec in self:
            rec.total = rec.debit + rec.credit
             
        