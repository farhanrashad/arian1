# -*- coding: utf-8 -*-

from odoo import api, models,modules,fields, _
from odoo.exceptions import UserError

class resPartnerInherit(models.Model):
    _inherit = 'res.partner'

    is_a_broker = fields.Boolean(string="Is a Broker")
    commission_calculation_method = fields.Selection([
        ('by_rate_uom' , 'By Rate / UOM'),
        ('by_per_age','By %age of Total Amount')
    ], string='Commission Calculation Method')
    commission_rate = fields.Float(string = 'Commission Rate')
    commission_per = fields.Float(string = 'Commission %age')
    commission_paid_on_purchases_account = fields.Many2one('account.account', string='Commission Paid on Purchases Account')


    @api.onchange('is_a_broker')
    def check_name(self):
        if self.is_a_broker != True:
            self.commission_paid_on_purchases_account = False
            self.commission_calculation_method = False
            self.by_rate_uom = False
            self.commission_rate = 0
            self.by_per_age = False
            self.commission_per = 0


    @api.model
    def create(self, values):
        if values['is_a_broker']:
            if not values['commission_paid_on_purchases_account']:
                raise UserError(('Please select any commission paid account member!'))
            if not values['commission_calculation_method']:
                raise UserError(('Please choose (By Rate / UOM) OR (By %age of Total Amount) !'))
            else:
                if values['commission_calculation_method'] == 'by_rate_uom':
                    if values['commission_rate']<=0:
                        raise UserError(('Please Enter some Commission Rate value!'))
                if values['commission_calculation_method'] == 'by_per_age':
                    if values['commission_per']<=0:
                        raise UserError(('Please Enter some Commission %age value!'))
        return super(resPartnerInherit, self).create(values)



    def write(self, values):

        flag1 = 2
        flag2 = 2
        flag3 = 2
        flag4 = 2
        flag5 = 2

        try:
            val = values['is_a_broker']
            flag1 = 1
            if val == False:
                flag1 = 0
        except:
            pass

        try:
            val = values['commission_paid_on_purchases_account']
            flag2 = 1
            if not val:
                flag2 = 0
        except:
            pass

        try:
            val = values['commission_calculation_method']
            flag3 = 1
            if not val:
                flag3 = 0
        except:
            pass

        try:
            if flag3 == 1:
                if values['commission_calculation_method'] == 'by_rate_uom':
                    if values['commission_rate'] <= 0:
                        flag4 = 1
                    else:
                        values['commission_per'] = 0
                        flag4 = 0
            else:
                if values['commission_rate'] <= 0:
                    flag4 = 1
        except:
            pass

        try:
            if flag3 == 1:
                if values['commission_calculation_method'] == 'by_per_age':
                    if values['commission_per'] <= 0:
                        flag5 = 1
                    else:
                        values['commission_rate'] = 0
                        flag5 = 0
            else:
                if values['commission_per'] <= 0:
                    flag5 = 1
        except:
            pass

        if flag1 != 0:
            if flag2 == 0:
                raise UserError(('Please select any commission paid account member!'))
            elif flag3 == 0:
                raise UserError(('Please choose (By Rate / UOM) OR (By %age of Total Amount) !'))
            elif flag4 == 1:
                raise UserError(('Please Enter some Commission Rate value!'))
            elif flag5 == 1:
                raise UserError(('Please Enter some Commission %age value!'))

        return super(resPartnerInherit, self).write(values)


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'
    broker_partner_ref = fields.Many2one('res.partner',string="Broker" ,domain = [('is_a_broker','=',True)])
    commission_method = fields.Selection(related='broker_partner_ref.commission_calculation_method')


    def action_view_invoice(self):
        if self.broker_partner_ref.id:
            commission_rate_uom_bill = self.broker_partner_ref.commission_rate
            commission_percent_age_bill = self.broker_partner_ref.commission_per
            total_commission=0
            if self.commission_method == 'by_rate_uom':
                total_qty = 0
                for line in self.order_line:
                    total_qty += line.product_qty
                total_commission = total_qty *commission_rate_uom_bill

            if self.commission_method == 'by_per_age':
                total_commission = self.amount_total *commission_percent_age_bill

            action = self.env.ref('account.action_move_in_invoice_type')
            result = action.read()[0]
            create_bill = self.env.context.get('create_bill', False)
            result['context'] = {
                'default_type': 'in_invoice',
                'default_company_id': self.company_id.id,
                'default_purchase_id': self.id,
                'default_partner_id': self.partner_id.id,
                'default_broker_partner_ref_bill' : self.broker_partner_ref.id,
                'default_commission_rate' : commission_rate_uom_bill,
                'default_commission_prcentage' : commission_percent_age_bill,
                'default_total_commission' : total_commission,
            }
        else:
            action = self.env.ref('account.action_move_in_invoice_type')
            result = action.read()[0]
            create_bill = self.env.context.get('create_bill', False)
            result['context'] = {
                'default_type': 'in_invoice',
                'default_company_id': self.company_id.id,
                'default_purchase_id': self.id,
                'default_partner_id': self.partner_id.id,
            }
        self.sudo()._read(['invoice_ids'])
        if len(self.invoice_ids) > 1 and not create_bill:
            result['domain'] = "[('id', 'in', " + str(self.invoice_ids.ids) + ")]"
        else:
            res = self.env.ref('account.view_move_form', False)
            form_view = [(res and res.id or False, 'form')]
            if 'views' in result:
                result['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
            else:
                result['views'] = form_view
            if not create_bill:
                result['res_id'] = self.invoice_ids.id or False
        result['context']['default_invoice_origin'] = self.name
        result['context']['default_ref'] = self.partner_ref
        return result

    # def action_view_invoice(self):
    #     res = super(PurchaseOrderInherit, self).action_view_invoice()
    #
    #     commission_rate_uom_bill = self.broker_partner_ref.commission_rate
    #     commission_percent_age_bill = self.broker_partner_ref.commission_per
    #
    #     if self.commission_method == 'by_rate_uom':
    #         pass
    #
    #     if self.commission_method == 'by_per_age':
    #         pass
    #
    #     return res


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    broker_partner_ref_bill = fields.Many2one('res.partner',string="Broker" ,readonly=True, domain = [('is_a_broker','=',True)])
    commission_rate = fields.Float(string = 'Commission Rate')
    commission_prcentage = fields.Float(string = 'Commission %age')
    total_commission = fields.Float(string = 'Total Commission')

# raise UserError((self.broker_partner_ref.commission_calculation_method))
# raise UserError((self.commission_method))
