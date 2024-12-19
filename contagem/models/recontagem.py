from odoo import _, api, fields, models

class Recontagem(models.Model):
    _description = "Recontagem do estoque"
    _inherit = 'stock.quant'

