# -*- coding: utf-8 -*-
{
    'name': "Security Group for Quantity Field",

    'summary': """
       This module will add a Security Group for Quantity Field """,

    'description': """
         This module will add a Security Group for Quantity Field
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    'category': 'Employee',
    'version': '13.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/allow_changes_in_quantity_po_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
