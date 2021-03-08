# -*- coding: utf-8 -*-
{
    'name': "Corresponding Account",
    'version': '14.0.0.0',
    'category': 'Account',
    'summary': 'Add corresponding account on jurnal items ',
    'sequence': 3,
    'description': """"  """,
    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",
#     'license': 'LGPL-3',
    'depends': ['base','account_accountant'],
    
    'data': [
        'views/account_move.xml',
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
}
