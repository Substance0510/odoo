from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductManufacturer(models.Model):
    _inherit = 'product.template'

    def get_manufacturers(self):
        manufacturers = []
        raw_data = self.env['product.manufacturer1'].search([])
        for rec in raw_data:
            manufacturers.append((rec.product_manufacturers, rec.product_manufacturers))
        return manufacturers if manufacturers else [('Nothing here :(', 'Nothing here :(')]

    def get_models(self):
        models = []
        raw_data = self.env['product.models'].search([])
        for rec in raw_data:
            models.append((rec.product_models, rec.product_models))
        return models if models else [('Nothing to show here :(', 'Nothing to show here :(')]

    @api.onchange('product_manufacturers')
    def get_selected_manufacturer(self):
        selected_manufacturer = self.env['product.manufacturer1'] \
            .search([('product_manufacturers', '=', self.product_manufacturers)])
        return {'domain': {'product_models': [('manufacturer_id', '=', selected_manufacturer)]}}

    @api.constrains('product_models')
    def check_models(self):
        if self.product_manufacturers:
            selected_manufacturer = self.env['product.manufacturer1'] \
                .search([('product_manufacturers', '=', self.product_manufacturers)])

            selected_model = self.env['product.models'] \
                .search([('product_models', '=', self.product_models)])

            if self.product_models and selected_manufacturer != selected_model.manufacturer_id:
                raise ValidationError('You need to choose the correct models.')

    product_manufacturers = fields.Selection(get_manufacturers,
                                            string='Manufacturer', required=True)

    product_models = fields.Selection(get_models, string='Models')

