# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import models, fields, tools


class Promocionesagregacion(models.Model):
    _inherit = "product.template"

    #total_net_sale = fields.Float(string='Total Sin Iva', readonly=True)
    promocion1 = fields.Char(string='Promocion 1')
    promocion2 = fields.Char(string='Promocion 2')
    promocion3 = fields.Char(string='Promocion 3')

    
    

  