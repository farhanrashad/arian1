# -*- coding: utf-8 -*-

{
    "name": "validate revert reconcilation",
    "category": 'Accounting',
    "summary": 'adding a button and  a state in header',
    "description": """
         This module is for adding a button and  a state in header.
    """,
    "sequence": 1,
    "author": "Dynexcel",
    "website": "http://www.dynexcel.co",
    "version": '14.0.0.0',
    "depends": ['base', 'account'],
    "data": [

        # 'security/ir.model.access.csv',
        'security/security.xml',
        # 'report/fleet_request_report.xml',
        # 'report/fleet_request_report_pdf.xml',
        # 'wizard/vehicle_request_wizard_view.xml',
        'view/validate_revert_view.xml',
    ],

    "price": 25,
    "currency": 'EUR',
    "installable": True,
    "application": True,
    "auto_install": False,
}

