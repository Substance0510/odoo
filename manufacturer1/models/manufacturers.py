from odoo import models, fields


class Manufacturer1(models.Model):
    _name = 'product.manufacturer1'
    _description = 'Product manufacturers'

    product_manufacturers = fields.Char(string='Manufacturer', required=True, size=30,
                                       help='Enter only one manufacturer.')
    _rec_name = 'product_manufacturers'  # displaying name in many2one fields. Default is 'name'.


class Models(models.Model):
    _name = 'product.models'
    _description = 'Models of manufacturers.'

    product_models = fields.Char(string='Model', required=True, size=100,
                                 help='Enter only one model.')

    manufacturer_id = fields.Many2one('product.manufacturer1', string='Manufacturer', required=True)
