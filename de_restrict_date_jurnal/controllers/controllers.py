# -*- coding: utf-8 -*-
# from odoo import http


# class DeRestrictDateJurnal(http.Controller):
#     @http.route('/de_restrict_date_jurnal/de_restrict_date_jurnal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_restrict_date_jurnal/de_restrict_date_jurnal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_restrict_date_jurnal.listing', {
#             'root': '/de_restrict_date_jurnal/de_restrict_date_jurnal',
#             'objects': http.request.env['de_restrict_date_jurnal.de_restrict_date_jurnal'].search([]),
#         })

#     @http.route('/de_restrict_date_jurnal/de_restrict_date_jurnal/objects/<model("de_restrict_date_jurnal.de_restrict_date_jurnal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_restrict_date_jurnal.object', {
#             'object': obj
#         })
