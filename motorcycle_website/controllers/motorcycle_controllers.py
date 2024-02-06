from odoo import http

class Motorcycle(http.Controller):

    @http.route('/hello_world/', auth='public', website=True, sitemap=True)
    def hellow_worl(self, **kw):
        return 'Hello World!'

    @http.route('/motorcycle/registry', auth='public', website=True, sitemap=True)
    def motorcycles(self, **kw):
        motorcycles = http.request.env['motorcycle.registry'].search([])
        return http.request.render('motorcycle_website.motorcycle_website',{
            'motorcycles_registries': motorcycles_registries
        })