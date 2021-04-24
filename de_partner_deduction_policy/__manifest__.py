# -*- coding: utf-8 -*-
{
    'name': "Partner Deduction Policy",

    'summary': """
        Partner Deduction Policy
        """,

    'description': """
        Partner Deduction Policy
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",


    'category': 'purchase',
    'version': '13.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
