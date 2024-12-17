from odoo import _, api, fields, models

class CustomStockQuant(models.Model):
    _inherit = 'stock.quant'

    state = fields.Selection(string="Status", selection=[
        ('draft', 'Draft'),
        ('cancel', 'Cancelled'),
        ('confirm', 'In Progress'),
        ('recounting', 'Recounting'),
        ('Conference', 'Conference'),
        ('done', 'Validated'),
    ])
