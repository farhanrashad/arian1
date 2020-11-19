# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'search sale ref',
    'category': 'Tools',
    'summary': 'extenting your search ',
    'description': """
This module is about extend your search.
""",
    'depends': ['purchase','de_mrp_saleref','stock','mrp'],
    'data': [
        'views/search_saleref.xml',
        'views/search_saleid.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
