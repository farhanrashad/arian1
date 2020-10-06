# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import datetime
from dateutil.relativedelta import relativedelta
import dateutil


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
        print('start', data['form'].get('date'))
        non_converted = str(data['form'].get('date'))
        converted_date = dateutil.parser.parse(non_converted).date()
        print('non', converted_date)
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

    def get_product_obj(self, id):
        obj = self.env['product.template'].search([('id','=',id)])
        return obj

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
        order_id = order[0]
        order_lines = self.env['sale.order.line'].search([('order_id', '=', order_id)])
        for line in order_lines:
            lines.append(line.product_id.product_tmpl_id.id)
            lines = list(dict.fromkeys(lines))
        return {
            'doc_ids': active_ids,
            'doc_model': 'sale.order',
            'docs': active_sale_order,
            'data': data,
            'values': lines,
            'get_product_obj': self.get_product_obj,
        }


class CycleGearProformaData(models.AbstractModel):
    _name = 'report.de_custom_proforma_invoice.cycle_gear_proforma'

    def get_product_obj(self, id):
        obj = self.env['product.template'].search([('id','=',id)])
        return obj

    @api.model
    def _get_report_values(self, docids, data=None):
        if not data.get('form'):
            raise UserError(_("Form content is missing, this report cannot be printed."))
        lines = []
        active_ids = self.env.context.get('active_ids', [])
        active_sale_order = self.env['sale.order'].browse(active_ids)
        order = data['form'].get('order_id')
        order_id = order[0]
        order_lines = self.env['sale.order.line'].search([('order_id', '=', order_id)])
        for line in order_lines:
            lines.append(line.product_id.product_tmpl_id.id)
            lines = list(dict.fromkeys(lines))
        company_id = self.env.company.id
        company = self.env['res.company'].search([('id', '=', company_id)])
        list_sizes = ['XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL', '5XL']
        return {
            'doc_ids': active_ids,
            'doc_model': 'sale.order',
            'docs': active_sale_order,
            'data': data,
            'company': company,
            'values': lines,
            'get_product_obj': self.get_product_obj,
            'list_sizes': list_sizes,
        }


class CommercialReportData(models.AbstractModel):
    _name = 'report.de_custom_proforma_invoice.commercial_report'

    def get_product_obj(self, id):
        obj = self.env['product.template'].search([('id','=',id)])
        return obj

    @api.model
    def _get_report_values(self, docids, data=None):
        if not data.get('form'):
            raise UserError(_("Form content is missing, this report cannot be printed."))
        lines = []
        active_ids = self.env.context.get('active_ids', [])
        active_sale_order = self.env['sale.order'].browse(active_ids)
        order = data['form'].get('order_id')
        order_id = order[0]
        order_lines = self.env['sale.order.line'].search([('order_id', '=', order_id)])
        for line in order_lines:
            lines.append(line.product_id.product_tmpl_id.id)
            lines = list(dict.fromkeys(lines))
        company_id = self.env.company.id
        print('company', company_id)
        company = self.env['res.company'].search([('id', '=', company_id)])
        list_sizes = ['XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL', '5XL']
        return {
            'doc_ids': active_ids,
            'doc_model': 'sale.order',
            'docs': active_sale_order,
            'data': data,
            'company': company,
            'values': lines,
            'get_product_obj': self.get_product_obj,
            'list_sizes': list_sizes,
        }
