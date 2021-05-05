# -*- coding: utf-8 -*-
{
    'name': "Manufacturer1",

    'summary': "Manufacturer Management Software"
        """Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': "A module that adds the ability to select and create the manufacturer and model."
        """
        Long description of module's purpose
        """,

    'author': "Anton",
    'website': "http://stormfirstblog.pythonanywhere.com/blog/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/manufactures.xml',
        'views/product_manufacturer.xml',
        'views/models.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
