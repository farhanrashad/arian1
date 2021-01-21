# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2019-today Dynexcel Business Solution <www.dynexcel.com>

#
#################################################################################

from odoo import api, fields, models, _

class ExtraIssuance(models.TransientModel):
    _name = "extra.issuance.wizard"
    _description = "Extra Issuance wizard"

    sale_id = fields.Many2one('sale.order',string='Sale Order', required='1', help='select start date')
    articles_lines = fields.One2many('extra.issuance.wizard.line', 'article_id')

    

    def check_report(self):
        data = {}
        data['form'] = self.read(['sale_id', 'articles_lines'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['sale_id', 'articles_lines'])[0])
        return self.env.ref('de_extra_issuance.open_extra_issuance_action').with_context(landscape=True).report_action(
            self, data=data, config=False)
    
    
class ExtraIssuanceLine(models.TransientModel):
    _name = "extra.issuance.wizard.line"
    _description = "Extra Issuance wizard line"  
    

    
    article_id = fields.Many2one('extra.issuance.wizard', string="Extra Issuance")
    product_id = fields.Many2one('product.product', string='Product',)
    quantity = fields.Float(string='Quantity')


