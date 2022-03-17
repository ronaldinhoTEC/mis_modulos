from odoo import models, fields

class Partner(models.Model):
    _name = "wb.partner"
    
    debt_collector = fields.Char("Cobrador")
    seller = fields.Char("Vendedor")
    