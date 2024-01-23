from odoo import fields, models

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motrcycle Registry"

    certificate_title = fields.Binary(string="Titulo de Propiedad", required=True)
    current_milleage = fields.Float(string="Millaje Actual")
    name = fields.Char(string="Nombre", required=True)
    last_name = fields.Char(string="Apellido", required=True)
    license_plate = fields.Char(string="Matricula")
    registry_date = fields.Date(string="Fecha de Registro")
    vin = fields.Char(string="VIN", required=True)