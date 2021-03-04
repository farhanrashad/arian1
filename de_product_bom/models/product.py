from odoo import fields, models
from odoo.exceptions import UserError


class ProductBom(models.Model):
    _inherit = 'product.template'


    def action_craete_bom(self):
        variants = self.env['product.product'].search([('product_tmpl_id','=',self.id)])
        bom_vals = []
        bom_exists = self.env['mrp.bom'].search([('product_tmpl_id', '=', self.id)])

        if not bom_exists:
            raise UserError("Please create atleast one bom:")
        for bom in variants:
            component_lines = []
            for line in bom_exists[0].bom_line_ids:
                component_lines.append((0,0,{
                    'product_id': line.product_id.id,
                    'product_qty': line.product_qty,
                }))
            variants_bom_exists = self.env['mrp.bom'].search([('product_tmpl_id', '=', self.id),('product_id','=',bom.id)])
            if not variants_bom_exists:
                vals = {
                    	'product_tmpl_id': self.id,
                        'product_id': bom.id,
                        'product_qty':   bom_exists[0].product_qty,
                        'type':  bom_exists[0].type,
                        'product_uom_id': bom_exists[0].product_uom_id.id,
                        'subcontractor_ids': bom_exists[0].subcontractor_ids,
                        'bom_line_ids': component_lines,
                        }
                generated_bom = self.env['mrp.bom'].create(vals)
            # raise UserError('BOM CREATED')

