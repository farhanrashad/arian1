# -*- coding: utf-8 -*-
{
    'name': "Account General Ledger",

    'summary': """
        Account in General Ledger
        """,

    'description': """
        This module add's up the account field in GL Report
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",
    'category': 'Accounting',
    'version': '13.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account','account_reports'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

}
