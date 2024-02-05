import re
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = "registry_number"
    _sql_constraints = [('vin_unique', 'UNIQUE(vin)', 'VIN number already exist..')]

    active = fields.Boolean(default=True)

    owner_id = fields.Many2one(comodel_name="res.partner", string="Owner", ondelete='restrict', required=True, store=True)
    owner_phone = fields.Char(related='owner_id.phone', string="Phone", readonly=True)
    owner_email = fields.Char(related='owner_id.email', string="Email", readonly=True)
    
    certificate_title = fields.Binary(string="Certificate Title")
    current_mileage = fields.Float(string="Current Mileage")
    date_registry = fields.Date(string="Registration Date")
    license_plate = fields.Char(string="Licence Plate")
    
    registry_number = fields.Char(string="Registry Number",
                                   default="MRN", copy=False, required=True, readonly=True)
    
    vin = fields.Char(string="VIN", required=True)

    make = fields.Char(string="Make", compute="_compute_fields", readonly=True, store=True)
    model = fields.Char(string="Model", compute="_compute_fields", readonly=True, store=True)
    year = fields.Char(string="Year", compute="_compute_fields", readonly=True, store=True)

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

    @api.depends('vin')
    def _compute_fields(self):
        for record in self:
            if record.vin and len(record.vin) >= 4:
                record.make = record.vin[0:2].upper()
                record.model = record.vin[2:4].upper()
                record.year = record.vin[4:6]
            else:
                record.make = ''
                record.model = ''
                record.year = ''
