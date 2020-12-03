# -*- coding: utf-8 -*-
{
    'name': "Work order",

    'summary': """
        Multiple Work order from single Production Order""",

    'description': """
        Multiple Work order from single Production Order
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp','sale','product','purchase','stock','mrp_workorder'],

    # always loaded
    'data': [
        'data/stock_picking_action.xml',
        'security/security.xml',
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
