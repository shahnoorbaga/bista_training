# -*- coding: utf-8 -*-
{
    'name': "bista_training",

    'summary': "learning odoo",

    'description': "To learn odoo",

    'author': "shahnoor",
    'website': "http://www.shahnoor.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/trainee_view.xml',
        'views/trainer_view.xml',
        'views/trainee_location_view.xml',
        'views/designation_view.xml',
        'views/training_subjects_view.xml',
        'views/training_topics_view.xml',
        'views/menu_item.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
