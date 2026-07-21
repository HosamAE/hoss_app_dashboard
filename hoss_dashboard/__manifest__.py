# -*- coding: utf-8 -*-
{
    "name": "Hoss Premium Home Menu Customizer",
    "summary": "Premium Glassmorphic Home Menu Theme & Customizer for Odoo 19",
    "description": """
Hoss Premium Home Menu Customizer
=================================
Re-imagine your Odoo landing page. The Hoss Premium Home Menu Customizer transforms the default, rigid, one-size-fits-all Odoo welcome screen into a beautiful, personalized, high-performance visual canvas.

Key Features:
- Real-time visual customizer accessible directly via a systray brush icon (no page reload).
- Fully configurable backgrounds (solid, gradient, wallpaper presets, or custom images).
- Glassmorphic card customizer (opacity, border styling, radius, and shadows).
- Adjustable Odoo app icon layouts, shapes (circular, rounded, square), and sizes.
- Custom greeting messages (title, subtitle, alignment) and live systray clock.
- Supports both personal user customization and locked global corporate themes via Odoo Access Rights.
- Fully compatible with Odoo Community and Enterprise.
    """,
    "author": "HosamAE",
    "website": "https://www.linkedin.com/in/hossameldeen-eissa/",
    "support": "hossama.eissa@gmail.com",
    "category": "Theme/Backend",
    "version": "19.0.1.0.0",
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
