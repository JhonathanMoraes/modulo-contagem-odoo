from odoo import api, fields, models

class Contagem(models.Model):
    _name = 'contagem'
    _description = "Contagem"
    _inherits = {
        'stock.quant' : 'product_id',
        'stock.quant': 'location_id',
    }

    conferencia_id = fields.Many2one(comodel_name="stock.quant", string="Conference")
    counted_quantity = fields.Float("Counted quantity")