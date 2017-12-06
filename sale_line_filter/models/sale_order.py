# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging
from openerp import SUPERUSER_ID


_logger = logging.getLogger(__name__)
# class sale_line_filter(models.Model):

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

    to_invoice = fields.Boolean("To invoice (fix)", default=True)

    @api.model
    def check_to_invoice(self) :
        res = self.search([('state', 'in', ('sale', 'done')), ('to_invoice', '=', True)], limit=500, order="requested_date asc")
        _logger.debug("NB SO TO COMPUTE")
        _logger.debug(len(res))
        for so in res :
            
            if len(so.invoice_ids) :
                _logger.debug(so)
                so.to_invoice = False