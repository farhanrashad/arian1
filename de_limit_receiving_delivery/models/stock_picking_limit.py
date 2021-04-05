from odoo.exceptions import UserError
#
# - * - coding: utf - 8 -*-

from odoo import models, fields, api, _
from odoo.tools import float_compare, float_is_zero


class de_limit_receiving_delivery(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        if self.picking_type_id.code == 'incoming':
            delivery_order_ids = self.env['stock.picking'].search(
                [('origin', '=', self.origin), ('picking_type_id.code', '=', 'outgoing'), ('state', '=', 'done')])
            for rec_prod in self.move_ids_without_package:
                bom_products = self.env['mrp.bom'].search([('product_id', '=', rec_prod.product_id.id),
                                                           ('type', '=', 'subcontract')])
                if bom_products:
                    for rec_bom in bom_products:
                        if delivery_order_ids:
                            for rec_do in delivery_order_ids:
                                for rec_prod_do in rec_do.move_line_ids_without_package:
                                    if rec_bom.product_id == rec_prod_do.product_id.id:
                                        if rec_prod.quantity_done <= rec_prod_do.qty_done:
                                            pass
                                        else:
                                            raise UserError("Product : " + str(
                                                rec_prod.name) + " cannot be received as its component have not been delivered yet")
                        else:
                            raise UserError("Product : " + str(
                                rec_prod.name) + " cannot be received as its component have not been delivered yet")
        res = super(de_limit_receiving_delivery, self).button_validate()
        return res
