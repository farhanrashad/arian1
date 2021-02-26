# -*- coding: utf-8 -*-

{
    "name": "Salary Increment",
    'version': '14.0.0.0',
    "category": 'Increment',
    "summary": ' Employee Increment',
    'sequence': 0,
    "description": """" De_Increment is an module that inherit with Employee
     module. The purpose of this module add one more tab "Incremant" 
       where it have a filed about wage increment and save all the data inside into it. 
        """,
    'category': 'productivity',

    "author": "Dynexcel",
    "website": "http://www.dynexcel.co",
    'license': 'LGPL-3',
    'depends': ['base', 'hr','hr_contract'],
    'data': [
        'data/increment_action.xml',
        'report/increment_report.xml',
        'security/ir.model.access.csv',
        'views/de_employee_increment.xml',


    ],

    "installable": True,
    "application": True,
    "auto_install": False,
}
