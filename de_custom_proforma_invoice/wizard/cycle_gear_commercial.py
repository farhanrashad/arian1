# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CycleCommercialInvoice(models.Model):
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

    @api.onchange('product_tmpl_ids')
    def get_product_template_ids(self):
        tmpl_ids = []
        self.model = self.env.context.get('active_model')
        rec = self.env[self.model].browse(self.env.context.get('active_id'))
        for line in rec.order_line:
            tmpl_ids.append(line.product_id.product_tmpl_id.id)
        tmpl_ids = list(dict.fromkeys(tmpl_ids))
        # self.commercial_ids = (0, 0, {
        #     'product_id': 12,
        # })
        # template = super(CycleCommercialInvoice, self).get_product_template_ids
        # for tmpl in tmpl_ids:
        #     print('tmp', tmpl, template.id)
        #     template.commercial_ids.create({
        #         'product_id': 12
        #     })
        # self.commercial_ids = (0,0, {
        #     'product_id':
        # })
        return {'domain': {'product_tmpl_ids': [('id', 'in', tmpl_ids)]}}

    # @api.onchange('get_product')
    # def _onchange_product_id(self):
    #     for rec in self:
    #         if rec.get_product:
    #             lines = [(5, 0, 0)]
    #             self.model = self.env.context.get('active_model')
    #             rec = self.env[self.model].browse(self.env.context.get('active_id'))
    #             # lines = []
    #             # print("self.product_id", self.product_id.product_variant_ids)
    #             for line in self.product_id.product_variant_ids:
    #                 val = {
    #                     'product_id': line.id,
    #                     'product_qty': 15
    #                 }
    #                 lines.append((0, 0, val))
    #             rec.appointment_lines = lines

    @api.onchange('get_product')
    def _onchange_get_product(self):
        if self.get_product == True:
            products = []
            # custom = [(5, 0, 0)]
            custom = []
            self.model = self.env.context.get('active_model')
            rec = self.env[self.model].browse(self.env.context.get('active_id'))
            for line in rec.order_line:
                products.append(line.product_id.product_tmpl_id.id)
            products = list(dict.fromkeys(products))
            print('pro', products)
            for prod in products:
                vals = {
                    'product_id': prod
                }
                custom.append((0, 0, vals))
            self.commercial_ids = custom

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
    advance_payment = fields.Float(string='Advance Payment')
    bank_id = fields.Many2one(comodel_name='account.journal', string='Bank', domain="[('type','=','bank')]")
    product_tmpl_ids = fields.Many2many(comodel_name='product.template', string='Product')
    get_product = fields.Boolean(string='All Products')
    commercial_ids = fields.One2many(comodel_name='cycle.commercial.line', inverse_name='commercial_id')


class CycleCommercialInvoiceLine(models.Model):
    _name = 'cycle.commercial.line'

    commercial_id = fields.Many2one(comodel_name='cycle.commercial.wizard')
    product_id = fields.Many2one(comodel_name='product.template', string='Product', required=True)
    qtn_ctn = fields.Float(string='Qtn/Ctn')
    ctn_no = fields.Float(string='Ctn No')
    lot_no = fields.Char(string='Lot No')

