# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    
    
    
class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'    
    
    
class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'
    
    
class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'    
    
    
class MrpProduction(models.Model):
    _inherit = 'mrp.production'      