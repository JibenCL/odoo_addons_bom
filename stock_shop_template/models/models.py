# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import date, datetime, timedelta
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT


# class stock_shop_template(models.Model):
#     _name = 'stock_shop_template.stock_shop_template'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

TEMPLATE_FLAG = "[template]"

class StockPicking(models.Model) :
	# _name = 'stock.picking'
	_inherit = 'stock.picking'

	@api.model
	def _cron_generate_provision(self) :
		day_today = date.today().weekday()
		for picking in self.search([('origin', 'ilike', TEMPLATE_FLAG)]) :
			day_picking = datetime.strptime(picking.min_date, DEFAULT_SERVER_DATETIME_FORMAT).weekday()
			if day_today == day_picking :
				new_picking = picking.copy()
				new_picking.origin = picking.origin[len(TEMPLATE_FLAG):]
				new_picking.min_date = date.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)