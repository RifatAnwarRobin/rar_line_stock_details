from odoo import models, fields, api,_

class StockPickingX(models.Model):
    _inherit = "stock.picking"


class StockMoveX(models.Model):
    _inherit = 'stock.move'
    
    sm_qty_available = fields.Float(
        related='product_id.free_qty',
        string='Available',
        readonly=True
    )

    def sm_action_view_stock_details(self):
        self.ensure_one()
        tree_view_id = self.env.ref('rar_line_stock_details.sm_view_stock_quant_location_tree').id
        action = {
            'name': 'Stock by Location',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'stock.quant',
            'domain': [
                ('product_id', '=', self.product_id.id),
                ('location_id.usage', '=', 'internal')
            ],
            'context': {'create': False, 'edit': False, 'delete': False},
            'views': [(tree_view_id, 'tree')],
            'target': 'new',
        }
        return action