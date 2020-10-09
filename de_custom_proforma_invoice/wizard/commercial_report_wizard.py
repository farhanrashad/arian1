# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CycleGearCommercialReport(models.TransientModel):
    _name = 'commercial.report.wizard'

    def action_print_cycle_gear_commercial_report(self):
        active_ids = self.env.context.get('active_ids', [])
        datas = {
            'ids': active_ids,
            'model': 'sale.order',
            'form': self.read()[0]
        }
        print('k2-->', datas)
        return self.env.ref('de_custom_proforma_invoice.commercial_report_action').report_action([], data=datas)

    proforma_invoice_no = fields.Char(string='Invoice NO')
    date = fields.Date(string='Date')
    po_no = fields.Char(string='P.O.No')
    form_date = fields.Date(string='Form-E Date')
    e_form = fields.Char(string='Form-E')
    invoice_date = fields.Date(string='Date')
    fcr_no = fields.Char(string='FCR NO')
    loading_port = fields.Char(string='Port of Loading')
    discharge_port = fields.Char(string='Port of Discharge')
    bl_no = fields.Char(string='BL No')
    bl_date = fields.Date(string='BL Date')
    shipment_of = fields.Char(string='Shipment of')
    ctn_no = fields.Float(string='No of Cartons')
    origin_country = fields.Char(string='Country of Origin')
    trade_term = fields.Char(string='Trade Terms')
    notify = fields.Char(string='Notify')
    notify_party = fields.Char(string='Notify Party')
    order_id = fields.Many2one(comodel_name='sale.order', string='Customer Order', required=True)
    bill_to = fields.Char(string='Bill To')
    ship_to = fields.Char(string='Ship To')
    income_terms = fields.Char(string='Income Terms')
    ship_via = fields.Char(string='Ship Via')
    payment_terms = fields.Char(string='Payment Terms')
    delivery_date = fields.Date(string='Delivery Date')
    cycle_gear_to = fields.Char(string='Cycle Gear To')
    sign_date = fields.Date(string='Date')
    sro_no = fields.Char(string='SRO No')
