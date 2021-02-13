# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name": "BOM",
    "category": 'product',
    "summary": 'product Summary',
    "description": """


    """,
    "sequence": 1,
    "author": "Dynexcel",
    "website": "http://www.dynexcel.co",
    "version": '14.1.0.0',
    "depends": ['base','product'],
    "data": [
         'views/product.xml',
         'security/ir.model.access.csv',
         'security/product_security.xml',
        # 'wizards/de_training_wizard.xml',


        # 'report/report_card.xml',
        # 'report/student_report_pdf.xml',
        # 'report/inherit_report_template.xml',

    ],


    "installable": True,
    "application": True,
    "auto_install": False,
}
