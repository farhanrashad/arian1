# -*- coding: utf-8 -*-
{
    'name': "Stock Restriction",

    'summary': """
        Stock Operation Restriction
        """,

    'description': """
        Stock Operation Restriction
        1- Nouman User have few difficulty in validating Picking Document
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '13.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','mrp','stock_account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
