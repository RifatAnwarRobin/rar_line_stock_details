# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class SaleOrderX(models.Model):
    _inherit = "sale.order"


class SaleOrderLineX(models.Model):
    _inherit = 'sale.order.line'
    
    sol_qty_available = fields.Float(
        related='product_id.free_qty',
        string='Available',
        readonly=True
    )

    def sol_action_view_stock_details(self):
        self.ensure_one()
        tree_view_id = self.env.ref('rar_line_stock_details.sol_view_stock_quant_location_tree').id
        action = {
            'name': 'Stock by Location',
            'type': 'ir.actions.act_window',
            'view_mode': 'list',
            'res_model': 'stock.quant',
            'domain': [
                ('product_id', '=', self.product_id.id),
                ('location_id.usage', '=', 'internal')
            ],
            'context': {'create': False, 'edit': False, 'delete': False},
            'views': [(tree_view_id, 'list')],
            'target': 'new',
        }
        return action

