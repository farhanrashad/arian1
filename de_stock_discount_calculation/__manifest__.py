# -*- coding: utf-8 -*-
{
    'name': "Stock Tax Calculation",

    'summary': """
        Stock Tax Calculation on Picking Document
        """,

    'description': """
        Stock Tax Calculation on Picking Document
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '13.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/delivery_slip_template.xml',
        'views/stock_picking_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
