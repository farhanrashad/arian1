# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ReportData(models.AbstractModel):
    _name = 'report.de_custom_proforma_invoice.custom_proforma_invoice1'
    _description = 'Report Data'

    def get_product_obj(self, id):
        obj = self.env['product.template'].search([('id','=',id)])
        return obj
    
    @api.model
    def _get_report_values(self, docids, data=None):
        if not data.get('form'):
            raise UserError(_("Form content is missing, this report cannot be printed."))

        values = []
        small_list = []
        large_list = []
        register_ids = self.env.context.get('active_ids', [])
        contrib_registers = self.env['sale.order'].browse(register_ids)
        date_from = data['form'].get('date', fields.Date.today())
        date_to = data['form'].get('date', str(datetime.now() + relativedelta(months=+1, day=1, days=-1))[:10])
        order = data['form'].get('proforma_invoice_no')
        order_id = order[0]
        order_lines = self.env['sale.order.line'].search([('order_id', '=', order_id)])
        for a1 in order_lines:
            values.append(a1.product_id.product_tmpl_id.id)
            values = list(dict.fromkeys(values))
        for value in values:
            # print('value', value.name)
            for line in order_lines:
                if line.product_id.product_tmpl_id.id == value:
                    small_list.append(line.product_id.id)
        return {
            'doc_ids': register_ids,
            'doc_model': 'sale.order',
            'docs': contrib_registers,
            'data': data,
            'values': values,
            'get_product_obj':self.get_product_obj,
            # 'lines_data': lines_data,
            # 'lines_total': lines_total
        }


class CycleGearCommercialInvoiceData(models.AbstractModel):
    _name = 'report.de_custom_proforma_invoice.cycle_gear_commercial'

    @api.model
    def _get_report_values(self, docids, data=None):
        if not data.get('form'):
            raise UserError(_("Form content is missing, this report cannot be printed."))
        lines = []
        active_ids = self.env.context.get('active_ids', [])
        active_sale_order = self.env['sale.order'].browse(active_ids)
        date_from = data['form'].get('date', fields.Date.today())
        date_to = data['form'].get('date', str(datetime.now() + relativedelta(months=+1, day=1, days=-1))[:10])
        order = data['form'].get('sale_order_id')
        print('order', order)
        order_id = order[0]
        print('order_id', order_id)
        order_lines = self.env['sale.order.line'].search([('order_id', '=', order_id)])
        print('order_lines', order_lines)
        for line in order_lines:
            lines.append(line.product_id.product_tmpl_id.id)
            lines = list(dict.fromkeys(lines))
        return {
            'doc_ids': active_ids,
            'doc_model': 'sale.order',
            'docs': active_sale_order,
            'data': data,
            'values': lines,
        }
