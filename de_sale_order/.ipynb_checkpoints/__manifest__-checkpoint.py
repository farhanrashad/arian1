# -*- coding: utf-8 -*-
{
    'name': "Sale Order product parent type",

    'summary': """
        this module is about to make total of products according to their parent type
        """,

    'description': """
        this module is about to make total of products according to their parent type
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '13.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],
   
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
