# -*- coding: utf-8 -*-

from odoo import api, models, modules,fields, _

class UsersExt(models.Model):
    _inherit = 'res.partner'

    region = fields.Selection([
        ('local' , 'Local'),
        ('foriegn','Foriegn')
    ], default='local', string="Region" ,required=True)
    

    mobile = fields.Char(required=True)
    category_id = fields.Many2many(required=True)
    street = fields.Char(required=True)
    street2 = fields.Char(required=True)
    city = fields.Char( required=True)

    property_supplier_payment_term_id = fields.Many2one( required=True)

