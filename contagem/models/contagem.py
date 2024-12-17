from odoo import _, api, fields, models

class Contagem(models.Model):
    _name = "contagem"
    _description = "Contagem de produtos"

    product = fields.Many2one('', string="Produto", required=True)
    location = fields.Many2many('', string="Local", required=True)
    counted_quantity = fields.Float(string="Quantidade contada")
    count_date = fields.Datetime(string="Data da contagem", default=lambda self: fields.datetime.now())