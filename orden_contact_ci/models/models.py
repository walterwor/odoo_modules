# -*- coding: utf-8 -*-

from odoo import models, fields, api

#class OrdenContact(models.Model):
#    _inherit = 'res.partner'

#    create_date
# class /mnt/extra-addons/orden_contact_ci(models.Model):
#     _name = '/mnt/extra-addons/orden_contact_ci./mnt/extra-addons/orden_contact_ci'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100