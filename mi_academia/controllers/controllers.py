# -*- coding: utf-8 -*-
# from odoo import http


# class MiAcademia(http.Controller):
#     @http.route('/mi_academia/mi_academia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mi_academia/mi_academia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mi_academia.listing', {
#             'root': '/mi_academia/mi_academia',
#             'objects': http.request.env['mi_academia.mi_academia'].search([]),
#         })

#     @http.route('/mi_academia/mi_academia/objects/<model("mi_academia.mi_academia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mi_academia.object', {
#             'object': obj
#         })
