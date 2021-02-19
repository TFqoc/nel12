# -*- coding: utf-8 -*-
from odoo import http

# class NelReports(http.Controller):
#     @http.route('/nel_reports/nel_reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nel_reports/nel_reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nel_reports.listing', {
#             'root': '/nel_reports/nel_reports',
#             'objects': http.request.env['nel_reports.nel_reports'].search([]),
#         })

#     @http.route('/nel_reports/nel_reports/objects/<model("nel_reports.nel_reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nel_reports.object', {
#             'object': obj
#         })