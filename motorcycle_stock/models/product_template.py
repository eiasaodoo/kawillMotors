from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    battery_capacity = fields.Selection(selection=[('xs', 'Small'),
                                ('0m', 'Medium'),
                                ('0l', 'Large'),
                                ('xl', 'Extra Large'),],
                                copy=False)
    
    charge_time = fields.Float()
    curb_weight = fields.Float()
    horsepower = fields.Float()
    launch_date = fields.Date()
    make = fields.Char()
    model = fields.Char()
    range = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    year = fields.Integer()

    detailed_type = fields.Selection(selection_add=[('motorcycle','Motorcycle')],
                            ondelete={'motorcycle': 'set default'},
                            help=".")
    
    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping
