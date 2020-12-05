# -*- coding: utf-8 -*-
#################################################################################
# Author      : Dynexcel (<https://dynexcel.com/>)
# Copyright(c): 2015-Present dynexcel.com
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
#################################################################################
from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PaymentState(models.Model):
    _name = 'account.payment_state'
    _description = 'Partners Payment'

    name = fields.Char(string='Payment Status',help='maintain the states of the payment document')
    authority = fields.Many2one('res.groups')

class account_payment(models.Model):
    _inherit = 'account.payment'
    _description = 'this class maintain the approvals of the payments. '

    state = fields.Selection([('draft', 'Draft'),
                              ('submit', 'Submit'),
                              ('approved', 'approved'),
                              ('posted', 'Posted'),
                              ('sent', 'Sent'),
                              ('reconciled', 'Reconciled'),
                              ('cancelled', 'Cancelled')],
                             readonly=True, default='draft', copy=False, string="Status", track_visibility='onchange')


    def action_draft(self):
        res = super(account_payment, self).action_draft()
        self.message_post(body=_('Dear %s, you are set payment to Draft.') % (self.env.user.name),
                          partner_ids=[self.env.user.partner_id.id])
        return res

#     @api.model
    def submit_payment(self):
        self.write({'state': 'submit'})
        self.message_post(body=_('Dear %s, payment is submitted for Approval.') % (self.env.user.name,),
                          partner_ids=[self.env.user.partner_id.id])

#     @api.model
    def approve_payment(self):
        self.write({'state': 'approved'})
        self.message_post(body=_('Dear %s, payment has approved.') % (self.env.user.name,),
                          partner_ids=[self.env.user.partner_id.id])

    # @api.multi
    # def cancel(self):
    #     for rec in self:
    #         for move in rec.move_line_ids.mapped('move_id'):
    #             if rec.invoice_ids:
    #                 move.line_ids.remove_move_reconcile()
    #             move.button_cancel()
    #             move.unlink()
    #         rec.state = 'cancelled'
    #
    # @api.multi
    # def unlink(self):
    #     if any(bool(rec.move_line_ids) for rec in self):
    #         raise UserError(_("You cannot delete a payment that is already posted."))
    #     if any(rec.move_name for rec in self):
    #         raise UserError(_(
    #             'It is not allowed to delete a payment that already created a journal entry since it would create a gap in the numbering. You should create the journal entry again and cancel it thanks to a regular revert.'))
    #     return super(account_payment, self).unlink()

    @api.model
    def just_create_payment(self):
        return True

#     @api.model
#     def post(self):
#         res = super(account_payment, self).post()
#         for order in self:
#             order.write({'state': 'draft'})
#             order.message_post(body=_('Dear %s, payment has posted') % (order.env.user.name,),
#                               partner_ids=[order.env.user.partner_id.id])
#         return res
    
    def post(self):
        """ Create the journal items for the payment and update the payment's state to 'posted'.
            A journal entry is created containing an item in the source liquidity account (selected journal's default_debit or default_credit)
            and another in the destination reconcilable account (see _compute_destination_account_id).
            If invoice_ids is not empty, there will be one reconcilable move line per invoice to reconcile with.
            If the payment is a transfer, a second journal entry is created in the destination journal to receive money from the transfer account.
        """
        AccountMove = self.env['account.move'].with_context(default_type='entry')
        for rec in self:

#             if rec.state != 'draft':
#                 raise UserError(_("Only a draft payment can be posted."))

            if any(inv.state != 'posted' for inv in rec.invoice_ids):
                raise ValidationError(_("The payment cannot be processed because the invoice is not open!"))

            # keep the name in case of a payment reset to draft
            if not rec.name:
                # Use the right sequence to set the name
                if rec.payment_type == 'transfer':
                    sequence_code = 'account.payment.transfer'
                else:
                    if rec.partner_type == 'customer':
                        if rec.payment_type == 'inbound':
                            sequence_code = 'account.payment.customer.invoice'
                        if rec.payment_type == 'outbound':
                            sequence_code = 'account.payment.customer.refund'
                    if rec.partner_type == 'supplier':
                        if rec.payment_type == 'inbound':
                            sequence_code = 'account.payment.supplier.refund'
                        if rec.payment_type == 'outbound':
                            sequence_code = 'account.payment.supplier.invoice'
                rec.name = self.env['ir.sequence'].next_by_code(sequence_code, sequence_date=rec.payment_date)
                if not rec.name and rec.payment_type != 'transfer':
                    raise UserError(_("You have to define a sequence for %s in your company.") % (sequence_code,))

            moves = AccountMove.create(rec._prepare_payment_moves())
            moves.filtered(lambda move: move.journal_id.post_at != 'bank_rec').post()

            # Update the state / move before performing any reconciliation.
            move_name = self._get_move_name_transfer_separator().join(moves.mapped('name'))
            rec.write({'state': 'posted', 'move_name': move_name})

            if rec.payment_type in ('inbound', 'outbound'):
                # ==== 'inbound' / 'outbound' ====
                if rec.invoice_ids:
                    (moves[0] + rec.invoice_ids).line_ids \
                        .filtered(lambda line: not line.reconciled and line.account_id == rec.destination_account_id and not (line.account_id == line.payment_id.writeoff_account_id and line.name == line.payment_id.writeoff_label))\
                        .reconcile()
            elif rec.payment_type == 'transfer':
                # ==== 'transfer' ====
                moves.mapped('line_ids')\
                    .filtered(lambda line: line.account_id == rec.company_id.transfer_account_id)\
                    .reconcile()

        return True
