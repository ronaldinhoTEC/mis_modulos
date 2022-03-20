# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Estudiante(models.Model):
    _name = 'colegio.estudiante'

    name = fields.Char()
    colegio_id= fields.Many2one("school.perfil", string="Nombre de Escuela", required=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
