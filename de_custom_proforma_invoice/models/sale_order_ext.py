# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
import dateutil


class SaleCustomProformaInvoice(models.Model):
    _inherit = 'sale.order'

    def pop_list(self, custom_list, a):
        custom_list.remove(a)
        return custom_list

    def custom_proforma_invoice1_button(self):
        wizard_view_id = self.env.ref(
            'de_custom_proforma_invoice.custom_proforma_invoice1_wizard')
        return {
            'name': _('Proforma Invoice'),
            'res_model': 'custom.proforma.invoice',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': wizard_view_id.id,
            'target': 'new',
        }

    def amount_to_text(self, amount, currency):
        convert_amount_in_words = amount_to_text_en.amount_to_text(amount, lang='en', currency='')
        convert_amount_in_words = convert_amount_in_words.replace(' and Zero Cent', ' Only ')
        convert_amount_in_words = convert_amount_in_words.replace('Cents', 'Dirhams Only ')
        return convert_amount_in_words

    def cycle_gear_commercial_invoice(self):
        prod_tmpl = []
        for line in self.order_line:
            prod_tmpl.append(line.product_id.product_tmpl_id.id)
        prod_tmpl = list(dict.fromkeys(prod_tmpl))
        wizard_view_id = self.env.ref(
            'de_custom_proforma_invoice.cycle_gear_commercial_invoice_wizard')
        tmpl_obj = self.env['product.template'].search([('id', 'in', prod_tmpl)])
        return {
            'name': _('Commercial Invoice'),
            'res_model': 'cycle.commercial.wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': wizard_view_id.id,
            'target': 'new',
            'context': {'default_get_product': True,
                        'default_sale_order_id': self.id},
        }

    def custom_proforma_cycle_gear(self):
        wizard_view_id = self.env.ref(
            'de_custom_proforma_invoice.cycle_gear_proforma_invoice_wizard')
        return {
            'name': _('Proforma Invoice'),
            'res_model': 'cycle.proforma.wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': wizard_view_id.id,
            'target': 'new',
        }


class SaleOrderLineExt(models.Model):
    _inherit = 'sale.order.line'

    qtn_ctn = fields.Float(string='Qtn/Ctn')
    ctn_no = fields.Float(string='Ctn No')
    lot_no = fields.Char(string='Lot No')
