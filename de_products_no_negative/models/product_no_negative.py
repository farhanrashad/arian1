
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    allow_negative_product = fields.Boolean(string="Allow Negative Product")