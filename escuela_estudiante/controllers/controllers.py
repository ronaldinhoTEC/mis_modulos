# -*- coding: utf-8 -*-
# from odoo import http


# class EscuelaEstudiante(http.Controller):
#     @http.route('/escuela_estudiante/escuela_estudiante', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escuela_estudiante/escuela_estudiante/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('escuela_estudiante.listing', {
#             'root': '/escuela_estudiante/escuela_estudiante',
#             'objects': http.request.env['escuela_estudiante.escuela_estudiante'].search([]),
#         })

#     @http.route('/escuela_estudiante/escuela_estudiante/objects/<model("escuela_estudiante.escuela_estudiante"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escuela_estudiante.object', {
#             'object': obj
#         })
