# -*- coding: utf-8 -*-
{
    'name': "Show Source/Origin on Journal Entries",
    'version': '14.0.0.0',
    'category': 'Account',
    'summary': 'To show PO source reference on journal entries.',
    'sequence': 3,
    'description': """"  """,
    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",
#     'license': 'LGPL-3',
    'depends': ['base','account_accountant','account'],
    
    'data': [
        'views/account_move_view.xml',
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
}
