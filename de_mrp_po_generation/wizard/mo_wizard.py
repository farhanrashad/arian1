# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#
# Order Point Method:
#    - Order if the virtual stock of today is below the min of the defined order point
#
from odoo import api, fields, models, _

from odoo import api, models, tools

import logging
import threading

_logger = logging.getLogger(__name__)


class StockSchedulerComputeSubcontract(models.TransientModel):
    _name = 'stock.scheduler.compute.subcontract'
    _description = 'Run Scheduler Manually Subcontract'
    
    
    
#     @api.model
    def procure_calculation(self):
        sale_order = self.env['sale.order'].search([('state','=','sale'),('is_processed','=', False)])
        if sale_order:
            for order in sale_order:
                vals = {
                    'date': fields.Date.today(),
                    'sale_id': order.id,
                }
                document = self.env['mrp.mo.beforehand'].create(vals)
                document.get_sheet_lines()
                document.action_generate_po()
                document.action_done()
            return document
        
        

