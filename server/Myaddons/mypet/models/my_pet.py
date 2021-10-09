# -*- coding: utf-8 -*-
from odoo import fields, models

class MyPet(models.Model):
    _name = "my.pet"
    _description = "My pet model"

    name = fields.Char('Myduyen', required=True)
    nickname = fields.Char('MyDuyen')
    description = fields.Text(' Description')
    age = fields.Integer('21', default=1)
    weight = fields.Float('52')
    dob = fields.Date('DOB', required=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='female')
    pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image")
    owner_id = fields.Many2one('res.partner', string='Owner')
    product_ids = fields.Many2many(comodel_name='product.product',
                                string="Related Products",
                                relation='pet_product_rel',
                                column1='col_pet_id',
                                column2='col_product_id')