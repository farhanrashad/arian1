# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo import exceptions
from odoo.exceptions import UserError


class RestrictCreateEdit(models.Model):
    _name = 'restrict.create.edit'


class StockPickingInh(models.Model):
    _inherit = 'stock.picking'

    restrict_create = fields.Boolean(string="Restrict", default=False)

    # def write(self, values):
    #     if not self.user_has_groups('de_restrict_create_edit.group_edit_access'):
    #         raise exceptions.ValidationError('Group is not allowed!')
    #     else:
    #         return super(StockPickingInh, self).write(values)

    # @api.model
    # def create(self, values):
    #     t_uid = self.env.uid
    #     if t_uid == 25:
    #         raise exceptions.ValidationError('You are not allowed to create customers / vendors')
    #     if t_uid == 12:
    #         raise exceptions.ValidationError('You are not allowed to create customers / vendors')
    #     if t_uid == 14:
    #         raise exceptions.ValidationError('You are not allowed to create customers / vendors')
    #     elif t_uid == 11:
    #         raise exceptions.ValidationError('You are not allowed to create customers / vendors')
    #     elif t_uid == 19:
    #         raise exceptions.ValidationError('You are not allowed to create customers / vendors')
    #     res = super(StockPickingInh, self).create(values)
    #     return res

    # @api.multi
    # def write(self, values):
    #     t_uid = self.env.uid
    #     if t_uid == 25:
    #         raise exceptions.ValidationError('You are not allowed to update customers / vendors')
    #     if t_uid == 12:
    #         raise exceptions.ValidationError('You are not allowed to update customers / vendors')
    #     if t_uid == 14:
    #         raise exceptions.ValidationError('You are not allowed to update customers / vendors')
    #     elif t_uid == 11:
    #         raise exceptions.ValidationError('You are not allowed to update customers / vendors')
    #     elif t_uid == 19:
    #         raise exceptions.ValidationError('You are not allowed to update customers / vendors')
    #     res = super(ResPartner, self).write(values)
    #     return res