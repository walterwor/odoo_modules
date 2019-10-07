# -*- coding: utf-8 -*-
{
    'name': "create_date_contact_ci",

    'summary': """
        Este modulo tiene como proposito proveer al usuario la posibilidad de 
        ordenar los contactos en función a la fecha de creación del mismo. """,

    'description': """
        Habilitar en el modo de vista de Lista - Arbol 
    """,

    'author': "Consultores Informaticos",
    'website': "https://www.consultoresinformaticos.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
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
        'demo/demo.xml',
    ],
    'auto_install': True,
}