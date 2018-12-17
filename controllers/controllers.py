# -*- coding: utf-8 -*-
from odoo import http

# class DlcSuite(http.Controller):
#     @http.route('/dlc__suite/dlc__suite/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dlc__suite/dlc__suite/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dlc__suite.listing', {
#             'root': '/dlc__suite/dlc__suite',
#             'objects': http.request.env['dlc__suite.dlc__suite'].search([]),
#         })

#     @http.route('/dlc__suite/dlc__suite/objects/<model("dlc__suite.dlc__suite"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dlc__suite.object', {
#             'object': obj
#         })