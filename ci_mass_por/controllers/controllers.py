# -*- coding: utf-8 -*-
from odoo import http

# class CiMassPor(http.Controller):
#     @http.route('/ci_mass_por/ci_mass_por/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ci_mass_por/ci_mass_por/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ci_mass_por.listing', {
#             'root': '/ci_mass_por/ci_mass_por',
#             'objects': http.request.env['ci_mass_por.ci_mass_por'].search([]),
#         })

#     @http.route('/ci_mass_por/ci_mass_por/objects/<model("ci_mass_por.ci_mass_por"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ci_mass_por.object', {
#             'object': obj
#         })