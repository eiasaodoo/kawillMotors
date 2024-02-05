# -*- coding: utf-8 -*-
# from odoo import http


# class MotorcycleStock(http.Controller):
#     @http.route('/motorcycle_stock/motorcycle_stock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/motorcycle_stock/motorcycle_stock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('motorcycle_stock.listing', {
#             'root': '/motorcycle_stock/motorcycle_stock',
#             'objects': http.request.env['motorcycle_stock.motorcycle_stock'].search([]),
#         })

#     @http.route('/motorcycle_stock/motorcycle_stock/objects/<model("motorcycle_stock.motorcycle_stock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('motorcycle_stock.object', {
#             'object': obj
#         })
