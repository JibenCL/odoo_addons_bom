# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from datetime import datetime, time, timedelta, date
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
import logging


_logger = logging.getLogger(__name__)


class MrpBomCostWizard(models.TransientModel):
    _name = "wizard.mrp_bom_cost"
    _description = "Mrp Bom Cost Wizard"

    bom = fields.Many2one('mrp.bom', string='Bom', required=True, default=lambda self : self.env.context.get('active_id', False))
    qty = fields.Integer('Quantity of finished product')

    @api.multi
    def print_report(self):

        return self.env['report'].get_action(self, 'bom_cost_qty.mrp_bom_cost', data={'qty' : self.qty,
                               'ids' : self.bom.ids})


class MrpBomCost(models.AbstractModel):
    _name = 'report.bom_cost_qty.mrp_bom_cost'

    @api.multi
    def get_lines(self, boms, qty):

        product_lines = []
        for bom in boms:
        	ration = qty and qty / bom.product_qty or 1
            products = bom.product_id
            if not products:
                products = bom.product_tmpl_id.product_variant_ids
            for product in products:
                attributes = []
                for value in product.attribute_value_ids:
                    attributes += [(value.attribute_id.name, value.name)]
                result, result2 = self.env['mrp.bom']._bom_explode(bom, product, 1)
                product_line = {'name': product.name, 'lines': [], 'total': 0.0,
                                'currency': self.env.user.company_id.currency_id,
                                'product_uom_qty': qty or bom.product_qty,
                                'product_uom': bom.product_uom,
                                'attributes': attributes}
                total = 0.0
                for bom_line in result:
                    line_product = self.env['product.product'].browse(bom_line['product_id'])
                    price_uom = self.env['product.uom']._compute_qty(line_product.uom_id.id, line_product.standard_price, bom_line['product_uom'])
                    line = {
                        'product_id': line_product,
                        'product_uom_qty': bom_line['product_qty'] * ratio,
                        'product_uom': self.env['product.uom'].browse(bom_line['product_uom']),
                        'price_unit': price_uom,
                        'total_price': price_uom * bom_line['product_qty'] * ratio,
                    }
                    total += line['total_price']
                    product_line['lines'] += [line]
                product_line['total'] = total
                product_lines += [product_line]
        return product_lines

    @api.multi
    def render_html(self, data=None):
        boms = self.env['mrp.bom'].browse(data and data.get("ids", False) or self.ids)
        qty = data and data.get("qty", False)
        res = self.get_lines(boms, qty)
        return self.env['report'].render('mrp.mrp_bom_cost', {'lines': res})