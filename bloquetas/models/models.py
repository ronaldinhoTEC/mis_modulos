# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Propiedades(models.Model):
    _name = 'bloquetas.propiedades'

    nombre = fields.Char("Nombre", required=True)
    medidas = fields.Char("Medidas:", required=True)
    cantidad = fields.Integer("Cantidad:", required=True)
    presupuesto = fields.Text("presupuesto:", required=True)
    tipo = fields.Selection([('casa', 'Casa'), ('edificio', 'Edificio')], string='Tipo de bloqueta')
    fecha = fields.Date()
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
