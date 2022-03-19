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
    
class Type(models.Model):
    
    _inherit = 'sale.order'
    
    partner_id = fields.Many2one(
        'bloquetas.propiedades',
        string='partner',
        )




