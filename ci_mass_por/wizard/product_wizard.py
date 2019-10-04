# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductWizard(models.TransientModel):
    _name = "product.wizard"

    def _value_products(self):
        return self.env['product.template'].browse(self.env.context.get('active_ids'))

    products_ids = fields.Many2many('product.template', string='Product', default=_value_products)
    percent = fields.Float('percent')

    @api.multi
    def set_price_percent(self):
        for record in self:
            if record.products_ids:
                for product in record.products_ids:
                    product.lst_price = product.lst_price * (1 + (self.percent / 100))
