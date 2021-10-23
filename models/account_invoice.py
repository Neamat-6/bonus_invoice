# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class AccountMoveLIne(models.Model):
    _inherit = 'account.move.line'

    bonus_check = fields.Boolean(string='Bonus')

    @api.onchange('bonus_check')
    @api.constrains('bonus_check')
    def change_price(self):
        for line in self:
            if line.bonus_check:
                line.price_unit = 0.0
                line.tax_ids = False
