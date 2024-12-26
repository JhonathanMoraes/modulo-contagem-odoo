from odoo import api, fields, models
from odoo.cli.scaffold import env

class Contagem(models.Model):
    _name = 'contagem'
    _description = "Contagem"

    conference_id = fields.Many2one(comodel_name="stock.quant", string="Conference ID")
    product_id = fields.Many2one(comodel_name="stock.quant", string="Product")
    location_id = fields.Many2one(comodel_name="stock.location", string="Location")
    user_id = fields.Many2one(comodel_name="res.users", string="User")
    counted_quantity = fields.Float("Counted quantity")
    type = fields.Selection(string="Type", required=True, default='counting', selection=[
        ('counting', 'Counting'),
        ('recounting', 'Recounting'),
        ('conference', 'Conference'),
    ])

    @api.model
    def create(self, vals_list):

        new_conference = env['stock.quant'].create({
            'product_id': self.product_id,
            'location_id': self.location_id,
            'quantity': 0.0,
        })
        return super(Contagem, self).create(vals_list)