from odoo import fields, models, _


class ForecastStock(models.Model):
    _inherit = 'product.product'
    

    forecast_stock = fields.Float(string='Stock ForeCast', compute = '_compute_forecast_stock')
    
    
    def _compute_forecast_stock(self):
        self.forecast_stock = 100
#         record = self.env['stock.location'].search([('location_id', '=', self.id)])
