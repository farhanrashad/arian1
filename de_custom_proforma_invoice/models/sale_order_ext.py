# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class SaleCustomProformaInvoice(models.Model):
    _inherit = 'sale.order'

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
        wizard_view_id = self.env.ref(
            'de_custom_proforma_invoice.cycle_gear_commercial_invoice_wizard')
        return {
            'name': _('Commercial Invoice'),
            'res_model': 'cycle.commercial.wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': wizard_view_id.id,
            'target': 'new',
        }
