# -*- coding: utf-8 -*-
{
    'name': "bloquetas",

    'summary': """
        Este modulo nos proporciona informacion importante sobre las
        propiedades de las bloquetas de ronaldinhoTEC""",

    'description': """
        Este modulo nos proporciona informacion importante sobre las
        propiedades de las bloquetas de ronaldinhoTEC, ademas de una funcion
        informativa que nos permite calcular el peso de una bloqueta 
        en base a su tamaño y su material.
    """,

    'author': "RonaldinhoTEC",
    'website': "https://ronaldinhotec.github.io/mi-portafolio/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'rTEC_modulos',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
