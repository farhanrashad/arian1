
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    no_negative_product = fields.Boolean(
        string="No Negative Product", default=True, help="Allows You to Prohibit Negative Product Quantities."
    )


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    no_negative_product = fields.Boolean(
        related="company_id.no_negative_product",
        string="No Negative Product",
        readonly=False,
        help="Allows You to Prohibit Negative Product Quantities.",
    )