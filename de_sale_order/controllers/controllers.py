# -*- coding: utf-8 -*-
# from odoo import http


# class DeSaleOrder(http.Controller):
#     @http.route('/de_sale_order/de_sale_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_sale_order/de_sale_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_sale_order.listing', {
#             'root': '/de_sale_order/de_sale_order',
#             'objects': http.request.env['de_sale_order.de_sale_order'].search([]),
#         })

#     @http.route('/de_sale_order/de_sale_order/objects/<model("de_sale_order.de_sale_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_sale_order.object', {
#             'object': obj
#         })
