# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from odoo import exceptions
from odoo.exceptions import UserError, ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    def action_update_operation(self):
        for record in self:
            line_data = []

            record.do_unreserve()
            for line in record.move_ids_without_package:
                line.update({
                  'state' : 'draft'

                  })
            for line in record.move_ids_without_package:
                line.unlink()  

            production_order = self.env['mrp.production'].search([('name','=',record.origin)])
            bom_id = self.env['mrp.bom'].search([('product_id','=',record.mo_product_id.id)])
            for bom_line in bom_id.bom_line_ids:
                line_data.append((0,0,{
                        'product_id': bom_line.product_id.id,
                        'name': bom_line.product_id.name,
                        'company_id': record.company_id.id,
    #                     'state': 'assigned',
                        'date': record.scheduled_date ,
                        'date_expected': record.scheduled_date ,
                        'location_dest_id': record.location_dest_id.id ,
                        'location_id': record.location_id.id,
                        'product_uom': bom_line.product_uom_id.id,
                        'product_uom_qty':  bom_line.product_qty * production_order.product_qty,
                    }))
            record.move_ids_without_package = line_data 
            record.update({
                  'state' : 'assigned'

                  })
            for line in record.move_ids_without_package:
                line.update({
                  'state' : 'confirmed'

                  })



class StockQuant(models.Model):
    _inherit = 'stock.quant'
    
    @api.model
    def create(self, values):
        t_uid = self.env.uid
        if self.user_has_groups('de_mrp_workorders.group_stock_quant_restrict'):
            raise exceptions.ValidationError('You are not allowed to create Stock')    
        res = super(StockQuant, self).create(values)
        return res
    
    
#     @api.multi
    def write(self, values):
        t_uid = self.env.uid
        if self.user_has_groups('de_mrp_workorders.group_stock_quant_restrict'):
            raise exceptions.ValidationError('You are not allowed to update Stock')
           
        res = super(StockQuant, self).write(values)
        return res




class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'
    
    qty_production = fields.Float('Original Production Quantity', readonly=True)
    is_ready = fields.Boolean(string="Is Ready")
    is_close = fields.Boolean(string="Is Close")
    
    
    def record_ready(self):
        if self.qty_producing == 0.0:
            raise exceptions.ValidationError('Please Input Quantity other than zero')
        elif  self.qty_producing > 0.0 :   
            self.update({
                'is_ready': True
            })

    
    
    def record_production(self):
        res = super(MrpWorkorder, self).record_production()
#         self.time_ids.date_end = datetime.today()
#         if self.is_last_unfinished_wo == True:
        qty_produced = 0.0
        finish_qty = 0.0
        raw_material =self.env['mrp.production'].search([('name','=',self.production_id.name)])
        for finish_line in raw_material.finished_move_line_ids:
            if finish_line.done_move == False:
                finish_qty = finish_qty + finish_line.qty_done
#         workorders = self.env['mrp.workorder'].search([('production_id.name','=',raw_material.name)])            
#         for workorder in workorders:
#             if self.env.context['active_id'] == self.env.context['active_id']:
#                 qty_produced = qty_produced + workorder.qty_produced
        for move_line in raw_material.move_raw_ids:
#                 if move_line.reserved_availability: 
#                     move_line.update({
#                         'quantity_done' : (move_line.reserved_availability/raw_material.product_qty)*qty_produced,
#                     })  
                
            if move_line.product_uom_qty:
                if move_line.is_done == False:
                    move_line.update({
                                'quantity_done' : (move_line.product_uom_qty_ratio)*finish_qty,
                            })
            else:
                 pass
#         if self.is_last_unfinished_wo == True:        
#         if self.state == 'done':
#             pass
#         else:
#             self.write({
#                    'state': 'done',
#                 })  
        self.update({
            'is_ready': False
        })         
        return res
    
    

    
    def do_finish(self):
        res = super(MrpWorkorder, self).do_finish()
        self.time_ids.date_end = datetime.today()
#         if self.is_last_unfinished_wo == True:
        qty_produced = 0.0
        finish_qty = 0.0
        raw_material =self.env['mrp.production'].search([('name','=',self.production_id.name)])
        for finish_line in raw_material.finished_move_line_ids:
            if finish_line.done_move == False:
                finish_qty = finish_qty + finish_line.qty_done
#         workorders = self.env['mrp.workorder'].search([('production_id.name','=',raw_material.name)])            
#         for workorder in workorders:
#             qty_produced = qty_produced + workorder.qty_produced
        for move_line in raw_material.move_raw_ids:
#                 if move_line.reserved_availability: 
#                     move_line.update({
#                         'quantity_done' : (move_line.reserved_availability/raw_material.product_qty)*qty_produced,
#                     })  
            if move_line.product_uom_qty: 
                if move_line.is_done == False:
                    move_line.update({
                            'quantity_done' : (move_line.product_uom_qty_ratio)*finish_qty,
                        })
                else:
                    pass
#         if self.is_last_unfinished_wo == True:        
        if self.state == 'done':
            pass
        else:
            self.write({
                   'state': 'done',
                })
#         self.update({
#             'is_ready': False
#         })    
            
        return res
    
    def action_open_manufacturing_order(self):
        res = super(MrpWorkorder, self).action_open_manufacturing_order()  
        finish_qty = 0.0
        raw_material =self.env['mrp.production'].search([('name','=',self.production_id.name)])
        for finish_line in raw_material.finished_move_line_ids:
            if finish_line.done_move == False:
                finish_qty = finish_qty + finish_line.qty_done
#         workorders = self.env['mrp.workorder'].search([('production_id.name','=',raw_material.name)]) 
#         qty_produced = 0.0
#         for workorder in workorders:
#             qty_produced = qty_produced + workorder.qty_produced
        for move_line in raw_material.move_raw_ids:
#             if move_line.reserved_availability: 
#                     move_line.update({
#                         'quantity_done' : (move_line.reserved_availability/raw_material.product_qty)*qty_produced,
#                     })  
            if move_line.product_uom_qty:
                if move_line.is_done == False:
                    move_line.update({
                        'quantity_done' : (move_line.product_uom_qty_ratio)*finish_qty,
                        })
                else:
                    pass
        return res


    
class StockMove(models.Model):
    _inherit = 'stock.move'
    
    product_uom_qty_ratio = fields.Float(string="Ratio", )
    products_qty = fields.Float(string="Order Quantity")
    product_uom_qty_planned_ratio = fields.Float(string="Planned Ratio")
    is_ratio = fields.Boolean(string="Is Ratio")
    
           
    




class MrpProduction(models.Model):
    _inherit = 'mrp.production'
    
    
    
    
    

    def action_assign(self):
        res = super(MrpProduction, self).action_assign()
        for move_line in self.move_raw_ids:
            if move_line.is_ratio == False:
                move_line.update({
                    'product_uom_qty_planned_ratio': move_line.reserved_availability/move_line.product_uom_qty_ratio,
                })
        workorders =self.env['mrp.workorder'].search([('production_id','=',self.name)])
        for workorder in workorders:
            for move_raw in self.move_raw_ids:
                for line in workorder.raw_workorder_line_ids:
                    if line.product_id == move_raw.product_id:
                        line.update({
#                                 'qty_reserved' : (move_raw.reserved_availability),
                            })
                    else:
                        pass
        return res
    
            
    def button_mark_done(self):
        for move_line in self.move_raw_ids:
            if move_line.product_uom_qty: 
                move_line.update({
#                     'quantity_done' : move_line.product_uom_qty,
                })
        ress = super(MrpProduction, self).button_mark_done()
       
        return ress  
    
   
    routing_f_id = fields.Many2one(
        'mrp.routing', srting='First Routing', store=True)
    routing_s_id = fields.Many2one(
        'mrp.routing', string='Second Routing', store=True)
    routing_t_id = fields.Many2one(
        'mrp.routing', string='Third Routing', store=True)
    routing_fo_id = fields.Many2one(
        'mrp.routing', string='Four Routing', store=True)
    product_f_qty = fields.Float(string='First Routing Quantity')
    product_s_qty = fields.Float(string='Second Routing Quantity')
    product_t_qty = fields.Float(string='Third Routing Quantity')
    product_fo_qty = fields.Float(string='Four Routing Quantity')
    
    
      
            
    
    
    @api.onchange('routing_f_id')
    def onchange_routing(self):
        if self.routing_f_id.id == 5:
            self.update({
                'routing_s_id': 6,
                'routing_t_id': 7,
                'routing_fo_id': 8,
            })
            
        elif self.routing_f_id.id == 6:
            self.update({
                'routing_s_id': 5,
                'routing_t_id': 7,
                'routing_fo_id': 8
            })
            
        elif self.routing_f_id.id == 7:
            self.update({
                'routing_s_id': 8,
                'routing_t_id': 5,
                'routing_fo_id': 6
            })
            
        elif self.routing_f_id.id == 8:
            self.update({
                'routing_s_id': 7,
                'routing_t_id': 5,
                'routing_fo_id': 6
            })

        elif self.routing_f_id.id == 9:
            self.update({
                'routing_s_id': 10,
                'routing_t_id': 11,
                'routing_fo_id': 12
            })

        elif self.routing_f_id.id == 10:
            self.update({
                'routing_s_id': 9,
                'routing_t_id': 11,
                'routing_fo_id': 12
            })
           
        elif self.routing_f_id.id == 11:
            self.update({
                'routing_s_id': 9,
                'routing_t_id': 10,
                'routing_fo_id': 12
            })

        elif self.routing_f_id.id == 12:
            self.update({
                'routing_s_id': 9,
                'routing_t_id': 10,
                'routing_fo_id': 11
            })
        
        else:
            pass
        

    
                
    def button_plans(self):


        total_quantity = 0.0
        total_processes_qty = 0.0
        finish_qty = 0.0
        minimum_planned = 0.0
        if self.product_f_qty:
            total_quantity = total_quantity + self.product_f_qty
        if self.product_s_qty:
            total_quantity = total_quantity + self.product_s_qty
        if self.product_t_qty:
            total_quantity = total_quantity + self.product_t_qty
        if self.product_fo_qty:
            total_quantity = total_quantity + self.product_fo_qty
            
        for line in self.move_raw_ids:
            minimum_planned = line.product_uom_qty_planned_ratio
            if line.product_uom_qty_planned_ratio > minimum_planned:
                pass
            else:
                minimum_planned = line.product_uom_qty_planned_ratio
 
            
        for finish_line in self.finished_move_line_ids:
            finish_qty = finish_qty + finish_line.qty_done
            
        total_processes_qty = total_processes_qty + minimum_planned
#         total_quantity = total_quantity + finish_qty
            
            
        if total_quantity > minimum_planned:
            raise exceptions.ValidationError('Failed to Plan. Please Check  if the components are reserved properly and the requested quantity to plan is not greater than total demand. You can only plan Quantity:' + str(minimum_planned) )            
        else:        
            if self.routing_f_id != '' and self.product_f_qty != 0.0:

                quantity = max(self.product_f_qty - sum(self.move_finished_ids.filtered(lambda move: move.product_id == self.product_id).mapped('quantity_done')), 0)
                quantity = self.product_id.uom_id._compute_quantity(quantity, self.product_uom_id)

                fval = {
                    'name': self.name,
                    'production_id': self.id,
                    'workcenter_id': self.routing_f_id.id,
    #                 'qty_production': self.product_f_qty,
                    'date_planned_start': self.date_planned_start,
                    'date_planned_finished': self.date_planned_start,                             
                    'product_uom_id': self.product_id.uom_id.id,
                    'is_user_working': True,
                    'quality_check_todo': True,
                    'is_last_step': True,
                    'skipped_check_ids': [],
                    'is_last_lot': True,
                    'operation_id': self.routing_f_id.operation_ids.id,
                    'duration_expected': self.routing_f_id.operation_ids.time_cycle,
                    'state':'ready' or 'pending',
                    'qty_production': self.product_f_qty,
                    'company_id': self.company_id.id,
                    'company_id': self.company_id.id,
                    'qty_remaining': self.product_f_qty,                            
                    'qty_producing': quantity,
                    'consumption': self.bom_id.consumption,
    #                  'raw_workorder_line_ids': [(0, 0, flines)]

                }
                workorders = self.env['mrp.workorder'].create(fval)
                for line in self.move_raw_ids:
                    for lines in self.bom_id.bom_line_ids:
                        quant= 0.0 
                        if line.product_id.id == lines.product_id.id:
                            quant = lines.product_qty
                            flines = {
                                'raw_workorder_id': workorders.id,
                                'product_id': line.product_id.id,
                                'qty_to_consume': (line.product_uom_qty_ratio) * self.product_f_qty ,
                                'qty_reserved': (line.product_uom_qty_ratio) * self.product_f_qty,

#                                 'qty_reserved': (line.reserved_availability / self.product_qty) * self.product_f_qty,
                                'product_uom_id': line.product_uom.id,
            #                     'qty_done': self.product_f_qty,

                            }

                            workorder_lines = self.env['mrp.workorder.line'].create(flines)
            else:
                pass

            if self.routing_s_id != '' and self.product_s_qty != 0.0:
                work_orders_line = self.env['mrp.workorder.line']
                quantity = max(self.product_s_qty - sum(self.move_finished_ids.filtered(lambda move: move.product_id == self.product_id).mapped('quantity_done')), 0)
                quantity = self.product_id.uom_id._compute_quantity(quantity, self.product_uom_id)

                sval = {
                    'name': self.name,
                    'production_id': self.id,
                    'workcenter_id': self.routing_s_id.id,
                    'date_planned_start': self.date_planned_start,
                    'date_planned_finished': self.date_planned_start,             
                    'product_uom_id': self.product_id.uom_id.id,
                    'is_user_working': True,
                    'quality_check_todo': True,
                    'is_last_step': True,
                    'skipped_check_ids': [],
                    'is_last_lot': True,
                    'operation_id': self.routing_s_id.operation_ids.id,
                    'duration_expected': self.routing_s_id.operation_ids.time_cycle,
                    'state':'ready' or 'pending',
                    'qty_production': self.product_s_qty,
                    'company_id': self.company_id.id,

                    'qty_remaining': self.product_s_qty,               
                    'qty_producing': quantity,
                    'consumption': self.bom_id.consumption,
    #                  'raw_workorder_line_ids': [(0, 0, slines)]

                }
                workorders = self.env['mrp.workorder'].create(sval)
                for line in self.move_raw_ids:
                    for lines in self.bom_id.bom_line_ids:
                        quant= 0.0 
                        if line.product_id.id == lines.product_id.id:
                            quant = lines.product_qty
                            slines = {
                                'raw_workorder_id': workorders.id,
                                'product_id': line.product_id.id,
                                'qty_to_consume': (line.product_uom_qty_ratio) * self.product_s_qty,
                                'qty_reserved': (line.product_uom_qty_ratio) * self.product_s_qty,
                                'product_uom_id': line.product_uom.id,
            #                     'qty_done': self.product_s_qty,
                            }
                            workorder_lines = self.env['mrp.workorder.line'].create(slines)
            else:
                pass

            if self.routing_t_id != '' and self.product_t_qty != 0.0:
                work_ordert_line = self.env['mrp.workorder.line']
                quantity = max(self.product_t_qty - sum(self.move_finished_ids.filtered(lambda move: move.product_id == self.product_id).mapped('quantity_done')), 0)
                quantity = self.product_id.uom_id._compute_quantity(quantity, self.product_uom_id)

                tval = {
                    'name': self.name,
                    'production_id': self.id,
                    'workcenter_id': self.routing_t_id.id,
                    'date_planned_start': self.date_planned_start,
                    'date_planned_finished': self.date_planned_start,
                    'company_id': self.company_id.id,
                    'product_uom_id': self.product_id.uom_id.id,
                    'operation_id': self.routing_t_id.operation_ids.id,
                    'duration_expected': self.routing_t_id.operation_ids.time_cycle,
                    'state':'ready' or 'pending',
                    'qty_production': self.product_t_qty,
                    'company_id': self.company_id.id,
                    'is_user_working': True,
                    'quality_check_todo': True,
                    'is_last_step': True,
                    'skipped_check_ids': [],
                    'is_last_lot': True,
                    'qty_remaining': self.product_t_qty,               
                    'qty_producing': quantity,
                    'consumption': self.bom_id.consumption,
    #                  'raw_workorder_line_ids': [(0, 0, tlines)]
                }
                workorders = self.env['mrp.workorder'].create(tval)
                for line in self.move_raw_ids:
                    for lines in self.bom_id.bom_line_ids:
                        quant= 0.0 
                        if line.product_id.id == lines.product_id.id:
                            quant = lines.product_qty
                            tlines = {
                                'raw_workorder_id': workorders.id,                    
                                'product_id': line.product_id.id,
                                'qty_to_consume': (line.product_uom_qty_ratio) * self.product_t_qty,
                                'qty_reserved': (line.product_uom_qty_ratio) * self.product_t_qty,
                                'product_uom_id': line.product_uom.id,       
            #                     'qty_done': self.product_t_qty,
                            }
                            workorder_lines = self.env['mrp.workorder.line'].create(tlines)
            else:
                pass

            if self.routing_fo_id != '' and self.product_fo_qty != 0.0:
                work_orderfo_line = self.env['mrp.workorder.line']
                quantity = max(self.product_fo_qty - sum(self.move_finished_ids.filtered(lambda move: move.product_id == self.product_id).mapped('quantity_done')), 0)
                quantity = self.product_id.uom_id._compute_quantity(quantity, self.product_uom_id)

                foval = {
                    'name': self.name,
                    'production_id': self.id,
                    'workcenter_id': self.routing_fo_id.id,
                    'date_planned_start': self.date_planned_start,
                    'date_planned_finished': self.date_planned_start,
                    'company_id': self.company_id.id,
                    'product_uom_id': self.product_id.uom_id.id,
                    'operation_id': self.routing_fo_id.operation_ids.id,
                    'duration_expected': self.routing_fo_id.operation_ids.time_cycle,
                    'state':'ready' or 'pending',
    #                 'qty_production': self.product_fo_qty,
                     'qty_production': self.product_fo_qty, 
                     'company_id': self.company_id.id,
                    'is_user_working': True,
                    'quality_check_todo': True,
                    'is_last_step': True,
                    'skipped_check_ids': [],
                    'is_last_lot': True,
                     'qty_remaining': self.product_fo_qty,               
                    'qty_producing': quantity,
                    'consumption': self.bom_id.consumption,
    #                 'raw_workorder_line_ids': [(0, 0, folines)]
                } 
                workorders = self.env['mrp.workorder'].create(foval)
                for line in self.move_raw_ids:
                    for lines in self.bom_id.bom_line_ids:
                        quant= 0.0 
                        if line.product_id.id == lines.product_id.id:
                            quant = lines.product_qty
                            folines = {
                                'raw_workorder_id': workorders.id,                    
                                'product_id': line.product_id.id,
                                'qty_to_consume': (line.product_uom_qty_ratio) * self.product_fo_qty ,
                                'qty_reserved':  (line.product_uom_qty_ratio) * self.product_fo_qty , 
                                'product_uom_id': line.product_uom.id,                  
            #                     'qty_done': self.product_fo_qty,                   
                            }
                            workorder_lines = self.env['mrp.workorder.line'].create(folines)
            else:
                pass

    
