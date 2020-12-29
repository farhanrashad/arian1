# -*- coding: utf-8 -*-
{
    'name': "Stock Approval",

    'summary': """
        This module is about to add new state in header named partially abailable""",

    'description': """
        This module is about to add new state in header named partially abailable
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",

    'category': 'Stock',
    'version': '13.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
#         'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

