# -*- coding: utf-8 -*-
{
    'name': "Line Stock Details Visibility",

    'summary': "This module enables the stock quantity available with location breakdown. Please see description of the module for details.",

    'description': """
        This module is used to Add the product stock quantity with a details viewing button. The Features Are Described Below:
        1. Sale Order Line Stock Availability
        2. Purchase Order Line Stock Availablity
        3. Inventory Operations Line (Stock Move) Stock Availablity.
    """,

    'author': "Rifat Anwar",
    'co-author': "Rifat Anwar",
    'website': "https://rifatanwar.odoo.com",
    'category': 'Inventory/Inventory',
    'license': 'LGPL-3',
    'version': '17.0.0.1',

    'depends': [
        'sale',
        'stock',
        'purchase',
        # 'mrp',
        # 'purchase_mrp'
        ],

    'data': [
        # 'security/ir.model.access.csv',
        'views/sol_view.xml',
        'views/pol_view.xml',
        'views/stock_move.xml',
        # 'views/mrp_production_view.xml',
    ],
    'icon': 'rar_line_stock_details/static/description/icon.png',
    'images': ['static/description/icon1.png'],
    
    'sequence':-199,
    'application': True,
    'installable': True,
    'auto_install': False,
    'price': 25.00,
    'currency': 'USD',
}