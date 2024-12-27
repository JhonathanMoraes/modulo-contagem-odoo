from itertools import product

from odoo import api, fields, models

class StockCount(models.Model):
    _name = 'stock.count'
    _description = "Contagem de estoque"

    stock_quant_id = fields.Many2one(comodel_name="stock.quant", string="Estoque Relacionado")
    product_id = fields.Many2one(comodel_name="product.product", string="Product", required=True)
    location_id = fields.Many2one(comodel_name="stock.location", string="Location", required=True)
    user_id = fields.Many2one(comodel_name="res.users", string="User", required=True)
    counted_quantity = fields.Float("Counted quantity", required=True)
    count_status = fields.Selection(string="Status", required=True, default='waiting', selection=[
        ('waiting', 'Waiting comparison'),
        ('wrong', 'Wrong quantities'),
        ('approved', 'Approved'),
        # ('closed', 'Closed')
    ])
    type = fields.Selection(string="Type", required=True, default='counting', selection=[
        ('counting', 'Counting'),
        ('recounting', 'Recounting'),
        ('conference', 'Conference'),
    ])

    @api.model
    def create(self, vals_list):
        stock_quant = self.env['stock.quant'].search([
            ('product_id', '=', vals_list.get('product_id')),
            ('location_id', '=', vals_list.get('location_id'))
        ], limit=1)

        if not stock_quant:
            stock_quant = self.env['stock.quant'].create({
                'product_id': vals_list.get('product_id'),
                'location_id': vals_list.get('location_id'),
                'quantity': 0.0,
            })

        vals_list['stock_quant_id'] = stock_quant.id

        return super(StockCount, self).create(vals_list)