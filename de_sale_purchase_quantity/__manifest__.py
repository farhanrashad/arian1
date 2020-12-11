# -*- coding: utf-8 -*-
{
    'name': "Order Quantities",

    'summary': """
       This module will add new fields  in form view """,

    'description': """
         This module will add new fields  in form view of sale order and purchase order
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale/Purchase',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase'],

    # always loaded
    'data': [
#         'security/ir.model.access.csv',
#         'security/training_security.xml',
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
