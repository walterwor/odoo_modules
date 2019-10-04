# -*- coding: utf-8 -*-

from odoo import models, fields, api


#class ProductWizard(models.Model):
#    _name = 'product.wizard'

#    def _value_products(self):
#        return self.env['product.template'].browse(self.env.context.get('active_ids'))

#    products_ids = fields.Many2many('products.template', string='Product', default=_value_products)
#    percent = fields.Char('percent')

#    @api.multi
#    def set_price_percent(self):
#        for record in self:
#            if record.products_ids:
#                for product in record.products_ids:
#                    product.lst_price = self.lst_price * self.percent
