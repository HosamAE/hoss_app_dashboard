# -*- coding: utf-8 -*-
{
    'name': 'Hoss App Dashboard',
    'summary': 'Premium Light Theme for Odoo Home Menu',
    'description': """
Hoss Premium Dashboard
=========================
Transforms the standard Odoo home menu into a beautiful, modern, glassmorphism-inspired dashboard.
    """,
    'author': 'Hoss',
    'website': 'https://hoss.dev',
    'support': 'support@hoss.dev',
    'category': 'Theme/Backend',
    'version': '19.0.1.0.0',
    'license': 'OPL-1',
    'price': 39.00,
    'currency': 'USD',
    'images': ['static/description/banner.png'],
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/hoss_dashboard_config_views.xml',
        'views/dashboard_action.xml',
        'views/res_users_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hoss_dashboard/static/src/css/home_menu.scss',
            'hoss_dashboard/static/src/js/dashboard_action.js',
            'hoss_dashboard/static/src/xml/dashboard_action.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
