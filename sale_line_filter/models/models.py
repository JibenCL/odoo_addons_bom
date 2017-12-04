# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class sale_line_filter(models.Model):
#     _name = 'sale_line_filter.sale_line_filter'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class SaleOrderLine(models.Model) :
    _inherit = 'sale.order.line'

    product_filter_regex = fields.Char("Filtre référence interne", default="EVENTS")

class SaleOrder(models.Model) :
    _inherit = 'sale.order'
    _name = 'sale.order'

    @api.one
    def copy(self, default=None):
        default = dict(default or {})
        default.setdefault('message_follower_ids', False)
        default.setdefault('partner_id', 37921)    
        default.setdefault('partner_shipping_id', 37921)    
        default.setdefault('partner_invoice_id', 37921)    
        return super(SaleOrder, self).copy(default)