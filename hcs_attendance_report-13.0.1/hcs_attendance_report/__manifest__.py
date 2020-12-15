# -*- coding: utf-8 -*-
{
    'name': "HCS Attendance Report",

    'summary': """
        Print Attendance Report for Employees""",

    'description': """
        This app helps you to print the attendances(Present and Absent Days) in PDF, based on Employees Calendar Resources.
    """,

    'author': "HCS",
    'website': "http://hcsgroup.io/",
    'company': 'Hafiz Consulting Services',
    'category': 'Employees',
    'version': '13.0.1',
    'depends': ['base', 'hr_attendance'],
    'license': 'AGPL-3',

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/report_views.xml',
    ],
    "application": True,
    "installable": True,
}
