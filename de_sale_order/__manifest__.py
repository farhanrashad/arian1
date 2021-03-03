# -*- coding: utf-8 -*-
{
    'name': "Sale Order Product Parent Type",

    'summary': """
        this module is about to make total of products according to their parent type
        """,

    'description': """
        this module is about to make total of products according to their parent type
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    'category': 'Sale',
    'version': '13.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],
   
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
    ],
}