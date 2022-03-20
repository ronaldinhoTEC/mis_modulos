# -*- coding: utf-8 -*-

from odoo import models, fields


class Escuela_perfil(models.Model):
    _name = 'school.perfil'

    nombre = fields.Char()
    email = fields.Char()
    phone = fields.Integer()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
