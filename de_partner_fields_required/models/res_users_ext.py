# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields, _

class UsersExt(models.Model):
    _inherit = 'res.partner'

    region = fields.Char(string="Region",required=True)

    mobile = fields.Char(required=True)
    category_id = fields.Many2many(required=True)
    street = fields.Char(required=True)
    street2 = fields.Char(required=True)
    city = fields.Char( required=True)
    # state_id = fields.Many2one(required=True)
    # zip = fields.Char( required=True)
    # country_id = fields.Many2one( required=True)

    property_supplier_payment_term_id = fields.Many2one( required=True)