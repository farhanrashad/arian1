# -*- coding: utf-8 -*-
# from odoo import http


# class DePurchaseBilling(http.Controller):
#     @http.route('/de_purchase_billing/de_purchase_billing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_purchase_billing/de_purchase_billing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_purchase_billing.listing', {
#             'root': '/de_purchase_billing/de_purchase_billing',
#             'objects': http.request.env['de_purchase_billing.de_purchase_billing'].search([]),
#         })

#     @http.route('/de_purchase_billing/de_purchase_billing/objects/<model("de_purchase_billing.de_purchase_billing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_purchase_billing.object', {
#             'object': obj
#         })
