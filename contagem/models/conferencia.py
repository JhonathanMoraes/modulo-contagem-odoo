from odoo import _, api, fields, models

class Conferencia(models.Model):
    _description = "Conferência das contagens"
    _inherit = 'stock.quant'
