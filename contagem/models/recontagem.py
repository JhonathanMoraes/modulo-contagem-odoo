from odoo import _, api, fields, models

class Recontagem(models.Model):
    _name = "recontagem"
    _description = "Recontagem dos produtos"
    _inherit = 'contagem'

    contagem_id = fields.Many2one("contagem", string="Contagem")