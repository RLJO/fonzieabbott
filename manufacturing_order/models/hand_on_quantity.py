import logging

from psycopg2 import Error, OperationalError

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression
from odoo.tools.float_utils import float_compare, float_is_zero, float_round






class StockQuant(models.Model):
    
    _inherit = 'stock.quant'

    inventory_quantity = fields.Float(string='Hand On quantity', compute='_compute_inventory_quantity')

    quantity = fields.Float(
        'Quantity',
        help='Quantity of products in this quant, in the default unit of measure of the product',
        readonly=True)
    


    @api.depends('quantity')
    def _compute_inventory_quantity(self):
        if not self._is_inventory_mode():
            self.inventory_quantity = 0
            return
        for quant in self:
            quant.inventory_quantity = quant.quantity
