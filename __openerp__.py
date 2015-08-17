# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Finalization state for Sale Orders',
    'category': 'Sales',
    'version': '1.0',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['sale_stock'],
    'description': """
Finalization state for Sale Orders
==================================
 * Adds a new state, 'Finalization', between Quotation Sent and Sale Order
 * Intended for situations where the Quotations needs changes before it gets converted to Sale Order (e.g. the customer approves the quote but with slight changes).

""",
    'data': [
        'view/sale_order.xml',
        'view/sale_report.xml',
        'workflow/sale_order_workflow.xml',
    ],

}
