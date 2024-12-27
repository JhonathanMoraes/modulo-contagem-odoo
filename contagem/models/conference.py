from odoo import api, fields, models

class Conference(models.Model):
    _description = "Conferência do estoque"
    _inherit = 'stock.quant'

    count_list = fields.One2many(comodel_name="stock.count", inverse_name="stock_quant_id", string="Contagens")

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

    def stock_count_form_action(self):
        for quant in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Contagem view',
                'view_mode': 'form',
                'res_model': 'stock.count',
                'view_id': self.env.ref('contagem.view_stock_count_form').id,
                'context': {
                    'default_product_id': quant.product_id.id,
                    'default_location_id': quant.location_id.id,
                }
        }


    def verify_counts(self):
        counts = self.env['stock.count'].search([('stock_quant_id', '=', self.id)])

        if self.env['stock.count'].search_count([('stock_quant_id', '=', self.id)]) >= 2:
            counts.write({'count_status': 'wrong'})

        count_map = {}
        for count in counts:
            if count.counted_quantity in count_map:
                count_map[count.counted_quantity].append(count.id)
            else:
                count_map[count.counted_quantity] = [count.id]

            if len(count_map[count.counted_quantity]) >= 2:
                self.env['stock.count'].browse(count_map[count.counted_quantity]).write({
                    'count_status': 'approved'
                })

                break

