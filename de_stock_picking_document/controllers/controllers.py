# -*- coding: utf-8 -*-
# from odoo import http


# class DeStockPickingDocument(http.Controller):
#     @http.route('/de_stock_picking_document/de_stock_picking_document/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_stock_picking_document/de_stock_picking_document/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_stock_picking_document.listing', {
#             'root': '/de_stock_picking_document/de_stock_picking_document',
#             'objects': http.request.env['de_stock_picking_document.de_stock_picking_document'].search([]),
#         })

#     @http.route('/de_stock_picking_document/de_stock_picking_document/objects/<model("de_stock_picking_document.de_stock_picking_document"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_stock_picking_document.object', {
#             'object': obj
#         })
