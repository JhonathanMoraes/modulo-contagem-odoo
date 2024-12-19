from odoo import _, api, fields, models

class Contagem(models.Model):
    _description = "Contagem do estoque"
    _inherit = 'stock.quant'

    state = fields.Selection(string="Status", readonly=True, default='confirm', selection=[
        ('confirm', 'Counting'),
        ('recounting', 'Recounting'),
        ('Conference', 'Conference'),
        ('done', 'Validated'),
    ])

    @api.onchange('product_id')
    def _onchange_product_id(self):
        pass

    @api.onchange('product_id')
    def _onchange_location_or_product_id(self):
        pass