# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Estudiante(models.Model):
    _name = 'escuela.estudiante'

    name = fields.Char()
    escuela_id= fields.Many2one("escuela.perfil", string="Nombre de Escuela", required=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
