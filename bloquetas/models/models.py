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
    
class Clientes(models.Model):
    _name = 'bloquetas.clientes'

    nombre = fields.Char("Nombre", required=True)
    apellido = fields.Char("Apellido", required=True)
    telefono = fields.Char("Telefono", required=True)
    # email = fields.Char("Email", required=True)
    # direccion = fields.Char("Direccion", required=True)
    # ciudad = fields.Char("Ciudad", required=True)
    # provincia = fields.Char("Provincia", required=True)
    # pais = fields.Char("Pais", required=True)
    # codigo_postal = fields.Char("Codigo Postal", required=True)
    # fecha = fields.Date()
    
