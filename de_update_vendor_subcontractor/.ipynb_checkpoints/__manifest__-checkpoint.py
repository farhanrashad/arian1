# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Vendor Subcontractor",

    'summary': """
       This module will add a check box fields  in form view and a security group for that """,

    'description': """
         This module will add a check box fields  in form view and a security group for that
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    'category': 'Employee',
    'version': '13.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','stock','mrp','purchase_stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/update_vendor_subcontractor_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
