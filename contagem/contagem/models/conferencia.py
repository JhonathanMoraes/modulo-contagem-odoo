from odoo import api, fields, models

class Conferencia(models.Model):
    _description = "Conferência do estoque"
    _inherit = 'stock.quant'

    state = fields.Selection(string="Status", readonly=True, default='confirm', selection=[
        ('confirm', 'Counting'),
        ('recounting', 'Recounting'),
        ('Conference', 'Conference'),
        ('done', 'Validated'),
    ])

    count_list = fields.One2many(comodel_name="contagem", inverse_name="conferencia_id", string="Contagens")

    @api.onchange('product_id')
    def _onchange_product_id(self):
        pass

    @api.onchange('product_id')
    def _onchange_location_or_product_id(self):
        pass

    def custom_stock_action(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'View conferencia Form',
            'view_mode': 'form',
            'res_model': 'stock.quant',
            'res_id': self.id
        }