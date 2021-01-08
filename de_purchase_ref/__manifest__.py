# -*- coding: utf-8 -*-
{
    'name': "Menufacturing Pivot Ref",

    'summary': """
        this module is about to add reference in pivot view and filter dropdown
        """,

    'description': """
        this module is about to add reference in pivot view and filter dropdown
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",


    'category': 'purchase',
    'version': '13.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp','stock'],

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
