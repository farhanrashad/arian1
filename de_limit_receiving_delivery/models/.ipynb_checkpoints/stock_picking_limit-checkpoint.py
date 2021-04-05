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
                [('origin', '=', self.name), ('picking_type_id.code', '=', 'outgoing'), ('state', '=', 'done')])
            for rec_prod in self.move_ids_without_package:
                if rec_prod.quantity_done != 0:
                    bom_products = self.env['mrp.bom'].search([('product_id', '=', rec_prod.product_id.id),
                                                               ('type', '=', 'subcontract')])
                    if bom_products:
                        for rec_bom in bom_products[0]:
                            if delivery_order_ids:
                                for rec_do in delivery_order_ids:
                                    for rec_prod_do in rec_do.move_line_ids_without_package:
                                        for rec_bom_lines in rec_bom.bom_line_ids:
                                            if rec_bom_lines.product_id.id == rec_prod_do.product_id.id:
                                                if rec_prod.quantity_done <= rec_prod_do.qty_done:
                                                    pass
                                                else:
                                                    raise UserError("Product : " + str(
                                                        rec_prod.name) + " cannot be received as in-sufficient components have been delivered.")
    #                                         else:
    #                                                 raise UserError(("asdee"))


                            else:
                                raise UserError("Product : " + str(
                                    rec_prod.name) + " cannot be received as no delivery document is found to send components to vendor first")
        res = super(de_limit_receiving_delivery, self).button_validate()
        return res
