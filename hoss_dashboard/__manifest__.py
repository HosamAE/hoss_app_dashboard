# -*- coding: utf-8 -*-
{
    "name": "Hoss Premium Home Menu Customizer",
    "summary": "Premium Glassmorphic Home Menu Theme & Customizer for Odoo 18",
    "description": """
Hoss Premium Home Menu Theme & Live Customizer
==============================================
Transforms the standard Odoo home menu into a beautiful, modern,
glassmorphism-inspired interface with live visual overrides.
    """,
    "author": "Hoss",
    "website": "https://www.linkedin.com/in/hossameldeen-eissa/",
    "support": "hossama.eissa@gmail.com",
    "category": "Theme/Backend",
    "version": "18.0.1.0.0",
    "license": "OPL-1",
    "price": 39.00,
    "currency": "USD",
    "images": ["static/description/banner.png"],
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/hoss_dashboard_config_views.xml",
        "views/dashboard_action.xml",
        "views/res_users_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "hoss_dashboard/static/src/css/home_menu.scss",
            "hoss_dashboard/static/src/js/dashboard_action.js",
            "hoss_dashboard/static/src/xml/dashboard_action.xml",
        ],
        "web.assets_web_dark": [
            "hoss_dashboard/static/src/css/home_menu_dark.scss",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
