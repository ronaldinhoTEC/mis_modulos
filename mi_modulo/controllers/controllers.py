# -*- coding: utf-8 -*-
# from odoo import http


# class MiModulo(http.Controller):
#     @http.route('/mi_modulo/mi_modulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mi_modulo/mi_modulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mi_modulo.listing', {
#             'root': '/mi_modulo/mi_modulo',
#             'objects': http.request.env['mi_modulo.mi_modulo'].search([]),
#         })

#     @http.route('/mi_modulo/mi_modulo/objects/<model("mi_modulo.mi_modulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mi_modulo.object', {
#             'object': obj
#         })
