from odoo import api, fields, models

class Conference(models.Model):
    _description = "Conferência do estoque"
    _inherit = 'stock.quant'

    count_list = fields.One2many(comodel_name="contagem", inverse_name="conference_id", string="Contagens")

    @api.onchange('product_id')
    def _onchange_product_id(self):
        pass

    @api.onchange('product_id')
    def _onchange_location_or_product_id(self):
        pass

    def stock_form_action(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Conferência view',
            'view_mode': 'form',
            'res_model': 'stock.quant',
            'res_id': self.id
        }

    def contagem_form_action(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Contagem view',
            'view_mode': 'form',
            'res_model': 'contagem'
        }