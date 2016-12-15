# -*- coding: utf-8 -*-
from openerp import http

# class LbsCustomModule(http.Controller):
#     @http.route('/lbs_custom_module/lbs_custom_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lbs_custom_module/lbs_custom_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lbs_custom_module.listing', {
#             'root': '/lbs_custom_module/lbs_custom_module',
#             'objects': http.request.env['lbs_custom_module.lbs_custom_module'].search([]),
#         })

#     @http.route('/lbs_custom_module/lbs_custom_module/objects/<model("lbs_custom_module.lbs_custom_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lbs_custom_module.object', {
#             'object': obj
#         })