# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging
from openerp import SUPERUSER_ID


_logger = logging.getLogger(__name__)
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

class ProductTemplate(models.Model) :
    _inherit = 'product.template'
#TODO : create product.tag model that inherits from another tag model
    tag_ids = fields.Many2many('crm.lead.tag', 'product_template_crm_tag', string='Tags', help="Optional tags you may want to assign for custom reporting")

    @api.model
    def force_tags(self) :
        products = self.search([('default_code', 'ilike', 'EVENTS')])
        _logger.debug(products)
        products.write({'tag_ids' : [(4,9, 0)]})

class SaleOrderLine(models.Model) :
    _inherit = 'sale.order.line'

    product_filter_regex = fields.Char("Filtre sur tags", default="EVENTS")

