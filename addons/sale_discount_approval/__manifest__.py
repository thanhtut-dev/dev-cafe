# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Loyalty Customization',
    'version': '16.0',
    'description': """
                This module extends from loyalty module with the feature of break discount in sales and pos.
    """,
    'depends': ['base', 'web', 'sale'],
    'data': [
        'views/loyalty_program_view.xml',
        ],
    'installable': True,
}
