from odoo import fields, models, _, api

class Major(models.Model):
    _name = 'school.major'
    _description = "Major"

    name = fields.Char(string="Majors Name", required=True)
    major_id = fields.Char(string='CN', required=True, copy=False, readonly=True,
                           default=lambda seft: _('New'))
    department_id = fields.Many2one('hr.department', 'Belonging Department', required=True)
    ology_id = fields.Many2one('school.ology', string="Belonging Ology", required=True)
    quantity_SV = fields.Integer("Quantity Student")
    quantity_GV = fields.Integer("Quantity Lecturer")

    @api.model
    def create(self, vals):
        if vals.get('major_id', ('New')) == ('New'):
            vals['major_id'] = self.env['ir.sequence'].next_by_code('school.major') or _('New')
        res = super(Major, self).create(vals)
        return res
