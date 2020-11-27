# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class update_vendor_ext(models.Model):
    _inherit = 'purchase.order'

    is_add_this_vendor_as_subcontactor = fields.Boolean(string="Add This Vendor As Subcontactor")
    order_set = fields.Boolean()

    def button_confirm(self):
        if self.is_add_this_vendor_as_subcontactor:

            for record in self.order_line:
                bom_product = self.env['mrp.bom'].search([('product_id', '=', record.product_id.id)])
                
                if bom_product:
                    partner_list = []

                    for partner_id in bom_product.subcontractor_ids:
                        partner_list.append(partner_id.id)

                    if self.partner_id.id not in partner_list:
                        partner_list.append(self.partner_id.id)

                    bom_product.subcontractor_ids = partner_list
                else:
                    new_record = self.env['mrp.bom'].create({
                        'product_tmpl_id':record.product_id.product_tmpl_id.id,
                        'product_id':record.product_id.id,
                        'product_qty':1,
                        'type':'subcontract',
                        'subcontractor_ids':[self.partner_id.id],
                    })

        rec = super(update_vendor_ext,self).button_confirm()

