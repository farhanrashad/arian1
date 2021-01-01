# -*- coding: utf-8 -*-
# import math
# from collections import defaultdict

from odoo import models,api, _
# from odoo import exceptions
from odoo.exceptions import UserError, ValidationError

class PurchaseOrderLineInherit(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_qty')
    def check_quantity(self):
        if self.state =='draft' or self.state =='sent' or self.user_has_groups('de_PO_ext.group_po_ext'):
            pass
        else:
            raise UserError(('Sorry! you are not allowed to make any changes in Quantity.'))

    @api.onchange('price_unit')
    def check_price(self):
        if self.state == 'draft' or self.state == 'sent' or self.user_has_groups('de_PO_ext.group_po_ext'):
            pass
        else:
            raise UserError(('Sorry! you are not allowed to make any changes in Price.'))

    class ItClusterExt(models.Model):
        _inherit = 'purchase.order'


