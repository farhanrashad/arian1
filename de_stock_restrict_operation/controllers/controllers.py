# -*- coding: utf-8 -*-
# from odoo import http


# class DeStockRestrictOperation(http.Controller):
#     @http.route('/de_stock_restrict_operation/de_stock_restrict_operation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_stock_restrict_operation/de_stock_restrict_operation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_stock_restrict_operation.listing', {
#             'root': '/de_stock_restrict_operation/de_stock_restrict_operation',
#             'objects': http.request.env['de_stock_restrict_operation.de_stock_restrict_operation'].search([]),
#         })

#     @http.route('/de_stock_restrict_operation/de_stock_restrict_operation/objects/<model("de_stock_restrict_operation.de_stock_restrict_operation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_stock_restrict_operation.object', {
#             'object': obj
#         })
