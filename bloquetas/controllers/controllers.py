# -*- coding: utf-8 -*-
# from odoo import http


# class Bloquetas(http.Controller):
#     @http.route('/bloquetas/bloquetas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bloquetas/bloquetas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bloquetas.listing', {
#             'root': '/bloquetas/bloquetas',
#             'objects': http.request.env['bloquetas.bloquetas'].search([]),
#         })

#     @http.route('/bloquetas/bloquetas/objects/<model("bloquetas.bloquetas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bloquetas.object', {
#             'object': obj
#         })
