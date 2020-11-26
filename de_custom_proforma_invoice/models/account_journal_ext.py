# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountJournalExt(models.Model):
    _inherit = 'account.journal'

    account_title = fields.Char(string='Account Title')
    swift_code = fields.Char(string='Swift Code')
