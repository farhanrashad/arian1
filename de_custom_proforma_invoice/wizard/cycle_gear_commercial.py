# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CycleCommercialInvoice(models.TransientModel):
    _name = 'cycle.commercial.wizard'

    def action_print_cycle_gear_commercial(self):
        active_ids = self.env.context.get('active_ids', [])
        datas = {
            'ids': active_ids,
            'model': 'sale.order',
            'form': self.read()[0]
        }
        print('k2-->', datas)
        return self.env.ref('de_custom_proforma_invoice.cycle_gear_commercial_invoice_action').report_action([], data=datas)

    invoice_id = fields.Char(string='Invoice')
    date = fields.Date(string='Date')
    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Sale Order')
    purchase_order_id = fields.Char(string='PO No')
    fca_price_total = fields.Float(string='Total FCA Sialkot Price')
    flight_no = fields.Char(string='Flight No')
    flight_date = fields.Date(string='Date')
    etd = fields.Char(string='ETD')
    eta = fields.Char(string='On/About ETA')
    issued_by = fields.Char(string='AWB Issued By')
    awb_no = fields.Char(string='AWB No')
    income_term = fields.Char(string='Income Term')
    payment_term = fields.Char(string='Payment Term')
    shipment_by = fields.Char(string='Shipment By')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    consigned_to = fields.Char(string='Consigned to the record of')
    credit_no = fields.Char(string='Drawn under irrovocable documentary credit (L/C no.)')
    issuance_date = fields.Date(string='Issue Date')
    proforma_invoice = fields.Char(string='Under Pro Forma invoice no')
    ctn_no = fields.Char(string='Total no. of CTNS')
