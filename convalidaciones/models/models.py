# -*- coding: utf-8 -*-

from odoo import models, fields


class Alumno(models.Model):
    _name = 'convalidaciones.alumno'
    
    name = fields.Char(string="Nombre y apellido")
    edad = fields.Integer(string="Edad")
    
class Curso(models.Model):
    _name = 'convalidaciones.curso'
    
    name = fields.Char(string="Nombre") 
    description = fields.Text(string="Descripcion del curso")
    
