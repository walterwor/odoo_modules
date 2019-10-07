# -*- coding: utf-8 -*-
from odoo import http

# class /mnt/extra-addons/ordenContactCi(http.Controller):
#     @http.route('//mnt/extra-addons/orden_contact_ci//mnt/extra-addons/orden_contact_ci/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/orden_contact_ci//mnt/extra-addons/orden_contact_ci/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/orden_contact_ci.listing', {
#             'root': '//mnt/extra-addons/orden_contact_ci//mnt/extra-addons/orden_contact_ci',
#             'objects': http.request.env['/mnt/extra-addons/orden_contact_ci./mnt/extra-addons/orden_contact_ci'].search([]),
#         })

#     @http.route('//mnt/extra-addons/orden_contact_ci//mnt/extra-addons/orden_contact_ci/objects/<model("/mnt/extra-addons/orden_contact_ci./mnt/extra-addons/orden_contact_ci"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/orden_contact_ci.object', {
#             'object': obj
#         })