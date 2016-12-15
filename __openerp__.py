# -*- coding: utf-8 -*-
{
    'name': "lbs_custom_module",

    'summary': """
        Module for customizing odoo 9 app.""",

    'description': """
        Custom stuff for odoo 9. Try README.md for more detailed information.
    """,

    'author': "LBS corporation",
    'website': "http://www.lbs.kiev.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/skype_field.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
