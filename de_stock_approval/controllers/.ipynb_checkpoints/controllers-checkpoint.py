# -*- coding: utf-8 -*-
# from odoo import http


# class DeStockApproval(http.Controller):
#     @http.route('/de_stock_approval/de_stock_approval/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_stock_approval/de_stock_approval/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_stock_approval.listing', {
#             'root': '/de_stock_approval/de_stock_approval',
#             'objects': http.request.env['de_stock_approval.de_stock_approval'].search([]),
#         })

#     @http.route('/de_stock_approval/de_stock_approval/objects/<model("de_stock_approval.de_stock_approval"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_stock_approval.object', {
#             'object': obj
#         })
