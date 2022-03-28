# -*- coding: utf-8 -*-

from odoo import models, fields


class Propiedades(models.Model):
    _name = 'bloquetas.propiedades'

    nombre = fields.Char("Nombre", required=True)
    medidas = fields.Char("Medidas:", required=True)
    cantidad = fields.Integer("Cantidad:", required=True)
    presupuesto = fields.Text("presupuesto:", required=True)
    tipo = fields.Selection([('casa', 'Casa'), ('edificio', 'Edificio')], string='Tipo de bloqueta')
    fecha = fields.Date()
    age_range_id = fields.Many2one(
        "res.partner.age.range", string="Age Range", required=True)
    





