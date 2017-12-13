# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class sale_service(models.Model):
#     _name = 'sale_service.sale_service'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class SaleOrderServiceLine(models.Model) :
	_name = "sale.order.service.line"

	order_id = fields.Many2one('sale.order', 'Source Sale Order', ondelete='cascade', required=True)
	employee_id = fields.Many2one('hr.employee', 'Waiter', ondelete='cascade', required=True)
	confirmed = fields.Boolean("Confirmed")
	phone = fields.Char(related='employee_id.address_id.phone', string='Phone')
	email = fields.Char(related='employee_id.address_id.email', string='Email')
	comment = fields.Char(string='Comment')


class SaleOrder(models.Model) :
	_inherit = 'sale.order'

	service_lines = fields.One2many('sale.order.service.line', 'order_id', "Waiters")