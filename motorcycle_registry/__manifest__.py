{
    'name': 'Motorcycle Registry',
    'summary': 'Manage Registration of Motorcycles.',
    'description': 'Motorcycle Registry\n================\nThis Modules is used to keep track of Motorcycle Registration and Ownership of each motorcycle of the brand.',
    'author': 'eiasaodoo',
    'version': '0.0.1',
    'license': 'OPL-1',
    'website': 'https://github.com/eiasaodoo/kawillMotors.git',
    'category': 'Kawill/Motorcycle Registry',
    'depends': ['base','contacts'],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'security/motorcycle_registry_security.xml',
        'data/motorcycle_registry_number_data.xml',
        'views/motorcycle_registry_menuitems.xml',
        'views/motorcycle_registry_views.xml',
        'reports/motorcycle_registry_report_templates.xml',
    ],
    'demo': [],
    'application': 'True'
}
