from odoo import _, api, fields, models


class Ology(models.Model):
    _name = "school.ology"
    _description = "Ology"

    name = fields.Char('Ology Name', required=True)
    ology_id = fields.Char(string='Ology Code', required=True, copy=False, readonly=True,
                           default=lambda seft: _('New'))

    department_id = fields.Many2one('hr.department', 'Belonging Department', required=True)
    major_quantity = fields.Integer('Major Quantity', required=True)
    major_list = fields.One2many('school.major', 'name', 'Major List', required=True)
    training_time = fields.Integer('Training Time', required=True)
    number_of_credits = fields.Integer('Number Of Credits', required=True)
    required_credits = fields.Integer('Required Credits')
    selected_credits = fields.Integer('Selected Credits')
    training_system = fields.Selection([
        ('one', 'Formal'),
        ('two', 'Unofficial'),
        ('three', 'High Quality'),
        ('four', 'Postgraduate'),
    ], string='Training System', default='one', required=True)

    @api.model
    def create(self, vals):
        if vals.get('ology_id', ('New')) == ('New'):
            vals['ology_id'] = self.env['ir.sequence'].next_by_code('school.ology') or _('New')
        res = super(Ology, self).create(vals)
        return res
