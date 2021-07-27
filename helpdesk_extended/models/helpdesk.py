# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class helpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
#     _description = 'help_desk_extended.help_desk_extended'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('stage_id')
#     @api.onchange('stage_id')
#     def _onchange_stage_id(self):
#         if self.stage_id
# #         for record in self:
# #             record.value2 = float(record.value) / 100


    @api.model
    def write(self, vals):
        res = super(helpdeskTicket, self).write(vals)        
        if vals.stage_id < self.stage_id:
            raise UserError('No se puede')
        return res
