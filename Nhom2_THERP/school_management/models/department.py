import datetime

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Department(models.Model):
    _inherit = "hr.department"
    _description = "Department"

    department_id = fields.Char(string='KH', required=True, copy=False, readonly=True,
                              default=lambda seft: _('New'))
    ology_list = fields.One2many('school.ology', 'name', 'Ology List', required=True)
    dean = fields.Char('Dean Name', size=128, required=True)
    dean_phone = fields.Char('Dean Phone', size=128, required=True)
    dean_email = fields.Char('Dean Email', size=128, required=True)
    deputy_dean = fields.Char('Deputy Dean Name', size=128, required=True)
    deputy_phone = fields.Char('Deputy Dean Phone', size=128, required=True)
    deputy_email = fields.Char('Deputy Dean Email', size=128, required=True)
    foundation_date = fields.Date('Foundation date', required=True)
    phone = fields.Char("Contact Phone", required=True)
    email = fields.Char("Contact Email", required=True)

    @api.model
    def create(self, vals):
        if vals.get('department_id', ('New')) == ('New'):
            vals['department_id'] = self.env['ir.sequence'].next_by_code('hr.department') or _('New')
        res = super(Department, self).create(vals)
        return res
