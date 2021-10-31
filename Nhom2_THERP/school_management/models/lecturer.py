import datetime

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Lecturer(models.Model):
    _inherit = "hr.employee"
    _description = "Lecturer"

    first_name = fields.Char('First Name', size=128, translate=True)
    middle_name = fields.Char('Middle Name', size=128)
    last_name = fields.Char('Last Name', size=128, required=True)
    lecturer_id = fields.Char(string='GV', required=True, copy=False, readonly=True,
                              default=lambda seft: _('New'))
    date_start = fields.Date("Date Start Work", required=True)
    date_end = fields.Date("Date End Work", required=False)
    homeroom_class = fields.Char("Homeroom Class", required=True)
    job = fields.Selection([
        ('one', 'Head Of Department'),
        ('two', 'Deputy Of Department'),
        ('three', 'Lecturer'),
        ('four', 'Tutors'),
        ('five', 'Party Secretary'),
        ('six', 'Secretary'),
        ('seven', 'Postgraduate')
    ], string='Position', required=True, default='three')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", tracking=True)
    age = fields.Integer(string='Age', compute="_get_age")
    ident_date = fields.Date(string='Identification Date')
    ident_place = fields.Char(string='Identification Place')
    graduate_major = fields.Char(string='Graduated Major', required=True)
    graduated_in = fields.Char(string='Graduated In')
    graduated_year = fields.Char(string='Graduated Year')
    recognition_in = fields.Char(string='Recognition In')
    recognition_year = fields.Char(string='Recognition Year')
    major_teaching = fields.Many2one('school.major', 'Major Teaching', required=True)
    language = fields.Char(string='Language')
    language_level = fields.Selection([
        ('one', 'Basic'),
        ('two', 'Intermediate'),
        ('three', 'High-Class'),
        ('four', 'Competently')
    ], string='Degree', default='four')
    is_the_union = fields.Boolean(string='Is The Union')
    day_into_party = fields.Date(string='Day Into Party')
    into_party_at = fields.Char(string='Into Party At')
    degree = fields.Selection([
        ('one', 'Professor'),
        ('two', 'Associate Professor'),
        ('three', 'Doctor'),
        ('four', 'Masters'),
        ('five', 'Bachelor'),
    ], string='Degree', required=True, default='three')
    work_status = fields.Selection([
        ('one', 'Contract'),
        ('two', 'Payroll')
    ], string='Work Status', required=True, default='one')
    religion = fields.Char(string="Religion")
    nation = fields.Char(string="Nation")
    email = fields.Char(string="Email")
    bank_acc_id = fields.Char(string="Bank Account")
    place_of_birth = fields.Char('Place of Birth', groups="hr.group_hr_user", tracking=True)
    temporary_address = fields.Char(string="Temporary Address", required=True)
    blood_group = fields.Selection([
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('AB+', 'AB+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB-', 'AB-')
    ], string='Blood Group')
    additional_note = fields.Text(string="Additional Note")
    study_at = fields.Boolean(string="Study At Da Nang University?")
    family_status = fields.Selection([
        ('normal', 'Normal'),
        ('poor_households', 'Poor Households'),
        ('near_poor_households', 'Near-poor Households'),
        ('family_difficult', 'Family Difficult'),
        ('orphan', 'Orphan'),
        ('ethnic_minority', 'Ethnic Minority')
    ], string='Family Status', default='normal')

    def copy(self, default={}):
        if self.lecturer_id == False:
            default['lecturer_id'] = str(self.id) + " (Copy)"
        else:
            default['lecturer_id'] = self.lecturer_id + " (Copy)"

        res = super(Lecturer, self).copy(default=default)
        return res

    @api.constrains('date_end')
    def onchange_end_dates(self):
        if (self.date_start and self.date_end) and (self.date_end < self.date_start):
            raise ValidationError(_('The end date must be greater or equal to the start date!'))

    @api.onchange('first_name', 'middle_name', 'last_name')
    def _onchange_name(self):
        if not self.middle_name:
            self.name = str(self.first_name) + " " + str(
                self.last_name)
        else:
            self.name = str(self.first_name) + " " + str(
                self.middle_name) + " " + str(self.last_name)

    @api.model
    def create(self, vals):
        if vals.get('lecturer_id', ('New')) == ('New'):
            vals['lecturer_id'] = self.env['ir.sequence'].next_by_code('hr.employee') or _('New')
        res = super(Lecturer, self).create(vals)
        return res

    def _get_age(self):
        today_date = datetime.date.today()
        for name in self:
            if name.birthday:
                birthday = fields.Datetime.to_datetime(name.birthday).date()
                age = str(int((today_date - birthday).days / 365))
                name.age = age
            else:
                name.age = ""
