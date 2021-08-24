# -*- coding: utf-8 -*-
{
    'name': "Cancel Multiple Journal Entries",
    'version': '14.0.0.0',
    'category': 'Account',
    'summary': 'To cancel multiple journal entries at time using server action.',
    'sequence': 3,
    'description': """"  """,
    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",
#     'license': 'LGPL-3',
    'depends': ['base','account_accountant','account'],
    
    'data': [
        'data/data.xml',
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
}
