# -*- coding: utf-8 -*-

{
    "name": "Salary Increment",
    'version': '13.0.0.0',
    "category": 'HR',
    "summary": ' Employee Increment',
    'sequence': 0,
    "description": """" De_Increment is an module that inherit with Employee
     module. The purpose of this module add one more tab "Incremant" 
       where it have a filed about wage increment and save all the data inside into it. 
        """,

    "author": "Dynexcel",
    "website": "http://www.dynexcel.co",
    'license': 'LGPL-3',
    'depends': ['base', 'hr','hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'data/increment_action.xml',
        'report/increment_report.xml',
        'views/de_employee_increment.xml',


    ],

    "installable": True,
    "application": True,
    "auto_install": False,
}
