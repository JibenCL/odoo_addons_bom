# -*- coding: utf-8 -*-
from openerp import http

# class StockShopTemplate(http.Controller):
#     @http.route('/stock_shop_template/stock_shop_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_shop_template/stock_shop_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_shop_template.listing', {
#             'root': '/stock_shop_template/stock_shop_template',
#             'objects': http.request.env['stock_shop_template.stock_shop_template'].search([]),
#         })

#     @http.route('/stock_shop_template/stock_shop_template/objects/<model("stock_shop_template.stock_shop_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_shop_template.object', {
#             'object': obj
#         })