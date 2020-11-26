# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Contacts fields',
    'category': 'Tools',
    'summary': 'extenting your address book',
    'description': """
This module is about to add 2 new fields and making 3 more fields mendatory.
""",
    'depends': ['base', 'mail'],
    'data': [
        'views/contact_views_ext.xml',
    ],
    'application': True,
}
