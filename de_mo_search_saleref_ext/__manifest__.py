# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'search sale ref',
    'category': 'Tools',
    'summary': 'extenting your search ',
    'description': """
This module is about extend your search.
""",
    'depends': ['purchase'],
    'data': [
        'views/search_saleref_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
