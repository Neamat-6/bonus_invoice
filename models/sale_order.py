# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    bonus_check = fields.Boolean(string='Bonus')

    @api.onchange('bonus_check')
    @api.constrains('bonus_check')
    def change_price(self):
        for line in self:
            if line.bonus_check:
                line.price_unit = 0.0
                line.tax_id = False

    def _prepare_invoice_line(self, qty):
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty=qty)
        for line in self:
            res['bonus_check'] = line.bonus_check
        return res
