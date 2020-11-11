# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductEnhancement(models.Model):
    _inherit = 'product.template'
    
    
    change_location = fields.Boolean(string="For Finished & Un-Finished Products")

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
