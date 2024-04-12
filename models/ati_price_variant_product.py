# -*- coding:utf-8 -*-
from odoo import fields, models, api 
from odoo.exceptions import UserError
from datetime import datetime

class AtiPriceVariantProduct(models.Model):
    _inherit = 'product.template'

    #Agregamos que el campo de standard_price sea store
    standard_price = fields.Float(string='Costo', store=True)

class AtiPriceVariantProductProduct(models.Model):
    _inherit = 'product.product'
    #agregamos que el campo de standard_price sea store y related en el campo de las demas variantes 
    standard_price = fields.Float(string='Costo', related='product_tmpl_id.standard_price', store=True)
