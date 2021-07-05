# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    aks_new_field = fields.Char(string="New Field")


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    aks_ref = fields.Char(string="Reference")