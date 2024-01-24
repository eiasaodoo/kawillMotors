from odoo import fields, models

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'

    certificate_title = fields.Binary(string="Titulo de Propiedad")
    current_mileage = fields.Float(string="Millaje Actual")
    name = fields.Char(string="Nombre", required=True)
    last_name = fields.Char(string="Apellido", required=True)
    license_plate = fields.Char(string="Matricula")
    registry_date = fields.Date(string="Fecha de Registro")
    vin = fields.Char(string="VIN", required=True)