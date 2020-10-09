# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CycleGearProformaWizard(models.TransientModel):
    _name = 'cycle.proforma.wizard'

    def action_print_cycle_gear_proforma(self):
        active_ids = self.env.context.get('active_ids', [])
        datas = {
            'ids': active_ids,
            'model': 'sale.order',
            'form': self.read()[0]
        }
        print('k3-->', datas)
        return self.env.ref('de_custom_proforma_invoice.cycle_gear_proforma_invoice_action').report_action([], data=datas)

    proforma_invoice_no = fields.Char(string='P.Invoice NO')
    date = fields.Date(string='Date', required=True)
    invoice_date = fields.Date(string='Invoice Date')
    order_id = fields.Many2one(comodel_name='sale.order', string='Customer Order', required=True)
    bill_to = fields.Char(string='Bill To')
    ship_to = fields.Char(string='Ship To')
    income_terms = fields.Char(string='Income Terms')
    ship_via = fields.Char(string='Ship Via')
    payment = fields.Char(string='Payment')
    delivery_date = fields.Date(string='Delivery Date')
