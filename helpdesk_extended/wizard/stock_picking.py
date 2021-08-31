# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)

class StockPicking(models.TransientModel):
    _name = 'create.stock.picking.return.wizard'
    
    
    origin = fields.Char('Razon de devolucion')
    partner_id = fields.Many2one('res.partner', 'Contact')
    location_id = fields.Many2one('stock.location', 'Return Location', domain="[('return_location', '=', True)]")
    move_ids_without_package = fields.One2many('stock.move', 'picking_id', string="Stock moves not in package", create=True)
    
    
    def action_create_stock_picking_return(self):
        vals = {
            'partner_id': self.partner_id.id,
            'picking_type_id': 1,
            'location_dest_id': self.location_id.id,
            'origin': self.reason
        }
        cra = self.env['stock.picking'].create(vals)
        return {
            'name': _('Return Picking Wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'stock.picking',
            'res_id': cra.id,
        }
