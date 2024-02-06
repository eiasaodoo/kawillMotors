{
    'name': "motorcycle_stock",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'author': "eiasaodoo",
    'version': '0.0.1',
    'license': 'OPL-1',
    'website': "https://github.com/eiasaodoo/kawillMotors.git",
    'category': 'Kawill/Motorcycle Registry',
    'depends': ['stock'],
    'data': [
        'views/product_template_inherit_views.xml',
    ],
    'demo': [],
    'auto_install': True
}
