# -*- coding: utf-8 -*-
# from odoo import http


# class DeSaleQuotationPrint2(http.Controller):
#     @http.route('/de_sale_quotation_print2/de_sale_quotation_print2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_sale_quotation_print2/de_sale_quotation_print2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_sale_quotation_print2.listing', {
#             'root': '/de_sale_quotation_print2/de_sale_quotation_print2',
#             'objects': http.request.env['de_sale_quotation_print2.de_sale_quotation_print2'].search([]),
#         })

#     @http.route('/de_sale_quotation_print2/de_sale_quotation_print2/objects/<model("de_sale_quotation_print2.de_sale_quotation_print2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_sale_quotation_print2.object', {
#             'object': obj
#         })
