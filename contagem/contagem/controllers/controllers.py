# -*- coding: utf-8 -*-
# from odoo import http


# class Contagem(http.Controller):
#     @http.route('/contagem/contagem', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contagem/contagem/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contagem.listing', {
#             'root': '/contagem/contagem',
#             'objects': http.request.env['contagem.contagem'].search([]),
#         })

#     @http.route('/contagem/contagem/objects/<model("contagem.contagem"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contagem.object', {
#             'object': obj
#         })
