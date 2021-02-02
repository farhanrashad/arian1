# -*- coding: utf-8 -*-
# from odoo import http


# class DeCrmContactsForm(http.Controller):
#     @http.route('/de_crm_contacts_form/de_crm_contacts_form/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_crm_contacts_form/de_crm_contacts_form/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_crm_contacts_form.listing', {
#             'root': '/de_crm_contacts_form/de_crm_contacts_form',
#             'objects': http.request.env['de_crm_contacts_form.de_crm_contacts_form'].search([]),
#         })

#     @http.route('/de_crm_contacts_form/de_crm_contacts_form/objects/<model("de_crm_contacts_form.de_crm_contacts_form"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_crm_contacts_form.object', {
#             'object': obj
#         })
