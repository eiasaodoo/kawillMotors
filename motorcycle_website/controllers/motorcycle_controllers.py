from odoo import http

class Motorcycle(http.Controller):
    
    @http.route('/motorcycles_registry', auth='public', website=True, sitemap=True)
    def motorcycles(self, **kw):
        motorcycles = http.request.env['motorcycle.registry'].search([])
        return http.request.render('motorcycle_website.motorcycle_registry', {
            'motorcycles': motorcycles
        })

class MotorcycleProduct(http.Controller):
   
    @http.route('/compare', auth='public', website=True, sitemap=True)
    def motorcycle_compare(self, **kw):
        product = http.request.env['product.template'].search([('detailed_type', '=', 'motorcycle')])
        motorcycles = product.search([('detailed_type', '=', 'motorcycle')])
        return http.request.render('motorcycle_website.motorcycle_compare', {
            'motorcycles': motorcycles
        })