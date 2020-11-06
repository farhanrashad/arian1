# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.exceptions import Warning

class ResUsers(models.Model):
    _inherit = 'res.users'

    restrict_locations = fields.Boolean('Restrict Location')

    stock_location_ids = fields.Many2many(
        'stock.location',
        'location_security_stock_location_users',
        'user_id',
        'location_id',
        'Stock Locations')

    default_picking_type_ids = fields.Many2many(
        'stock.picking.type',  string='Default Operations Type')


# class stock_move(models.Model):
#     _inherit = 'stock.move'
#     @api.constrains('state', 'location_id', 'location_dest_id')
#     def check_user_location_rights(self):
        
#         for stock in self:
#             stock.ensure_one()
#             if stock.state == 'draft':
#                 return True
#             if stock.picking_id.picking_type_code =='internal':
#                 return True
#             user_locations = stock.env.user.stock_location_ids
#             print(user_locations)
#             if stock.env.user.restrict_locations:
#                 message = _(
#                     'Invalid Location. You cannot process this move since you do '
#                     'not control the location "%s". '
#                     'Please contact your Adminstrator.')
#                 if stock.location_id not in user_locations:
#                     raise Warning(message % stock.location_id.name)
#                 elif stock.location_dest_id not in user_locations:
#                     raise Warning(message % stock.location_dest_id.name)


