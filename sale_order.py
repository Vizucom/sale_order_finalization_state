# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class sale_order(osv.Model):

    _inherit = 'sale.order'

    def action_finalization(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'finalization' }, context=context)

    ''' Add new state to the list '''
    _columns = {
        'state': fields.selection([
            ('draft', 'Draft Quotation'),
            ('sent', 'Quotation Sent'),
            ('finalization', _('Finalization Phase')),
            ('cancel', 'Cancelled'),
            ('waiting_date', 'Waiting Schedule'),
            ('progress', 'Sales Order'),
            ('manual', 'Sale to Invoice'),
            ('shipping_except', 'Shipping Exception'),
            ('invoice_except', 'Invoice Exception'),
            ('done', 'Done'),
            ], 'Status', readonly=True, track_visibility='onchange',
            help="Gives the status of the quotation or sales order. \nThe exception status is automatically set when a cancel operation occurs in the processing of a document linked to the sales order. \nThe 'Waiting Schedule' status is set when the invoice is confirmed but waiting for the scheduler to run on the order date.", select=True),
    }
