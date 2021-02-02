# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, datetime, timedelta
import dateutil.parser
from odoo.exceptions import UserError


class crmLeadInherit(models.Model):
    _inherit = 'res.partner'

    phone = fields.Char(string = "Home Number")
    mobile = fields.Char(string = "Mobile Number")
    date_of_birth = fields.Char(string = "DOB")
    ssn = fields.Char(string = "SSN")

    company_service = fields.Char(string = "Service Company")
    service_plan_id = fields.Many2one('res.service.plan', string = "Service Plan")

    service_price = fields.Char(string = "Service Price")
    order_date = fields.Datetime(string = "Order Date")
    
    shipping_id = fields.Many2one('res.shipping', string="Expect Shipping By")

    install_date = fields.Datetime(string = "Install Date")
    current_company = fields.Char(string = "Current Company")
	
    contract_term = fields.Selection([
       
    ], string = "Contract Term")
    billing_cycle = fields.Selection([
       
    ], string="Billing Cycle")
    
    contract_terms = fields.Selection([
       ('months_36' , 'Months 36'),
        ('months_60' , 'Months 60'),
    ], string = "Contract Term")
    billing_cycles = fields.Selection([
       ('monthly' , 'Monthly'),
        ('quartely' , 'Quartely'),
    ], string="Billing Cycle")
    
    billing_date = fields.Datetime(string = "Billing Date")
    payment_type = fields.Char(string = "Payment Type")
    notes = fields.Char(string = "Notes")
    
   

    @api.onchange('order_date')
    def seven_days_ahead_date(self):
        try:
            self.install_date = self.order_date + timedelta(days=7)
        except:
            pass
    
class ResCompanyService(models.Model):
    _name = 'res.company.service'
    description = 'res company service'
   
    name = fields.Char(string="Company Service")
 
class ResServicePlan(models.Model):
    _name = 'res.service.plan'
    description = 'res service plan'
   
    name = fields.Char(string="Service Plan")
 
 
class ResShipping(models.Model):
    _name = 'res.shipping'
    description = 'res shipping'
   
    name = fields.Char(string="Expect Shipping By")
    


