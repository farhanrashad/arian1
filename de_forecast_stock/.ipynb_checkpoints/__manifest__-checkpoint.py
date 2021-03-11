# -*- coding: utf-8 -*-
{
    'name': "Forecast Stock",
    'summary': """Purchase Order Based On Sale Order
    """,
    'sequence': '1',
    'description': """
    
    """,
    'category': 'Productivity',
    "author": "Dynexcel",
    "website": "http://www.dynexcel.co",
    'version': '13.0.0.1',
    
    'depends': [ 'sale'],
    
    'data': [
        'views/forecast_stock.xml',
    ],

    'installable': 'True',
    'application': 'True',
    'auto-install': False,
}
