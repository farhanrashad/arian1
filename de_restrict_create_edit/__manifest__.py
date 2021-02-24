{
    "name": "Restrict Access",
    "category": 'Stock',
    "summary": 'Restrict Create/Edit on Stock',
    "description": """


    """,
    "sequence": 0,
    "author": "Dynexcel",
    "website": "http://www.dynexcel.co",
    "version": '14.1.0.0',
    "depends": ['stock'],
    "data": [

        'security/ir.model.access.csv',
        'security/security.xml',
        'views/stock_picking_view.xml',

    ],

    "price": 25,
    "currency": 'PKR',
    "installable": True,
    "application": True,
    "auto_install": False,
}
