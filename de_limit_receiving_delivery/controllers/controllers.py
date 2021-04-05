# -*- coding: utf-8 -*-
# from odoo import http


# class DeLimitReceivingDelivery(http.Controller):
#     @http.route('/de_limit_receiving_delivery/de_limit_receiving_delivery/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_limit_receiving_delivery/de_limit_receiving_delivery/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_limit_receiving_delivery.listing', {
#             'root': '/de_limit_receiving_delivery/de_limit_receiving_delivery',
#             'objects': http.request.env['de_limit_receiving_delivery.de_limit_receiving_delivery'].search([]),
#         })

#     @http.route('/de_limit_receiving_delivery/de_limit_receiving_delivery/objects/<model("de_limit_receiving_delivery.de_limit_receiving_delivery"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_limit_receiving_delivery.object', {
#             'object': obj
#         })
