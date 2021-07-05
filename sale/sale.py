# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import Warning

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    aks_new_field = fields.Char(string="New Field")


    @api.model_create_multi
    def create(self, vals):
        print("This is debugging on my sale_inhrit module>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(vals)
        val_dict = vals and vals[0]
        val_dict['signed_by'] ='Jamshid K'
        return super(SaleOrder, self).create(vals)

    def split_char(self,word):
        word_list=[ch for ch in word]
        print(word_list)
        return word_list and word_list[1]
    def write(self, vals):
        print("HI  i am debugging when sale order edit from sale inherit module>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        ver=self.aks_new_field
        ver_no=self.split_char(ver) or 0
        ver_no = int(ver_no) +1
        if ver_no:

            new_ver = 'v'+ str(ver_no)
            vals['aks_new_field'] = new_ver
        return super(SaleOrder, self).write(vals)

    def unlink(self):
        print("Debugging when deleteing sale order")
        raise Warning("Deleting Blocked for Sale Order")
        return super(SaleOrder, self).unlink()



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    aks_ref = fields.Char(string="Reference")