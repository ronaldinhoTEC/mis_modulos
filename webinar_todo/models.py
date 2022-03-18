from odoo import models, fields

class Todo(models.Model):
    _name = "wb.todo"
    
    name = fields.Char("Nombre")
    status = fields.Selection(selection=[("borrador","Borrado"),("hecho","Hecho")])
    owner = fields.Char("Dueño")
    title = fields.Char("Titulo")
    price = fields.Selection(selection=[("minimo","1000"),("maximo","2000")])
    country = fields.Char("Pais")