# -*- coding: utf-8 -*-

from odoo import models, fields


class EscuelaPerfil(models.Model):
    _name = 'escuela.perfil'
    _description = 'escuela.escuela'

    nombre = fields.Char()
    email = fields.Char()
    phone = fields.Integer()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
