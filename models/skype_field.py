# -*- coding: utf-8 -*-

from openerp import api
from openerp.osv import osv, fields

class skype_field(osv.Model):
    _inherit = 'res.partner'

    _columns = {'skype_field': fields.char('Skype')}