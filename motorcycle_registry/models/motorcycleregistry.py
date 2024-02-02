import re
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = "registry_number"
    _sql_constraints = [('vin_unique', 'UNIQUE(vin)', 'VIN number already exist..')]


    active = fields.Boolean(default=True)

    certificate_title = fields.Binary(string="Certificate Title")
    current_mileage = fields.Float(string="Current Mileage")
    date_registry = fields.Date(string="Registration Date")
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    license_plate = fields.Char(string="Licence Plate")
    
    registry_number = fields.Char(string="Registry Number",
                                   default="MRN", copy=False, required=True, readonly=True)
    
    vin = fields.Char(string="VIN", required=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('motorcycle.registry.number')
        return super().create(vals_list)

    @api.constrains('license_plate', 'vin')
    def _check_validations(self):
        vin_pattern = re.compile(r'^[A-Z]{2}[A-Z]{2}\d{2}[A-Z\d]{2}\d{5}$')
        license_plate_pattern = re.compile(r'^[A-Z]{1,4}\d{1,3}[A-Z]{0,2}$')
    
        for record in self:
            if not vin_pattern.match(record.vin):
                raise ValidationError("VIN must follow the pattern: 2 uppercase letters, 2 uppercase letters, "
                                      "2 digits or 2 alphanumeric characters and 5 digits.")
            if not license_plate_pattern.match(record.license_plate):
                raise ValidationError("The license plate must follow the pattern: 1 to 4 uppercase letters, "
                                      "1 to 3 digits, followed by up to 2 optional uppercase letters.")

