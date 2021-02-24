# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo import exceptions
from odoo.exceptions import UserError


class RestrictCreateEdit(models.Model):
    _name = 'restrict.create.edit'


class StockPickingInh(models.Model):
    _inherit = 'stock.picking'

    restrict_create = fields.Boolean(string="Restrict", default=False)

    def write(self, values):
        if not self.user_has_groups('de_restrict_create_edit.group_edit_access'):
            pass
        else:
            raise exceptions.ValidationError('Group is not allowed!')