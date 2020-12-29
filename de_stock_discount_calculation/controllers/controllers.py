# -*- coding: utf-8 -*-
# from odoo import http


# class DeStockDiscountCalculation(http.Controller):
#     @http.route('/de_stock_discount_calculation/de_stock_discount_calculation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_stock_discount_calculation/de_stock_discount_calculation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_stock_discount_calculation.listing', {
#             'root': '/de_stock_discount_calculation/de_stock_discount_calculation',
#             'objects': http.request.env['de_stock_discount_calculation.de_stock_discount_calculation'].search([]),
#         })

#     @http.route('/de_stock_discount_calculation/de_stock_discount_calculation/objects/<model("de_stock_discount_calculation.de_stock_discount_calculation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_stock_discount_calculation.object', {
#             'object': obj
#         })
