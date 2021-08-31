# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)

class helpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    def write(self, vals):
        if self.env.user.has_group('helpdesk.group_helpdesk_manager'):
            return super(helpdeskTicket, self).write(vals)
        else:
            if int(vals['stage_id']) < self.stage_id.id:
                raise UserError('No puede devolver el estado del ticket si no pertenece al grupo administrador de mesa de ayuda.')