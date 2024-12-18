from odoo import _, api, fields, models

class Contagem(models.Model):
    _name = "contagem"
    _description = "Contagem de produtos"
    _inherit = 'stock.quant'

    state = fields.Selection(string="Status", readonly=True, default='confirm', selection=[
        ('confirm', 'Counting'),
        ('recounting', 'Recounting'),
        ('Conference', 'Conference'),
        ('done', 'Validated'),
    ])
