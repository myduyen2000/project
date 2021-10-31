from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Term(models.Model):
    _name = "school.term"
    _description = "Term"

    kyhoc = fields.Char('Semester', required=True)
    tenhp = fields.Char("Course's name", required=True)
    mahp = fields.Char('Course Code', required=True)
    sotc = fields.Integer('Number Of Credits', required=True)
    loaihp = fields.Selection([
        ('chuyennganh', 'Major'),
        ('binhthuong', 'Normal'),
        ('khac', 'Others')
    ], string='Loại học phần', default='Major')
    sotlt = fields.Integer('Number Of Theoretical Periods', required=True)
    sotth = fields.Integer('Number Of Pactice Periods', required=True)
    ghichu = fields.Selection([
        ('moi', 'Learn New'),
        ('lai', 'Learn Again'),
        ('caithien', 'Larn Improvement')
    ], string='Status', default='Learn New')
    tgbd = fields.Date('Start Time', required=False)
    tgkt = fields.Date('End time', required=False)
    lich = fields.Char('Schedule', required=True)
    phong = fields.Char('Room', required=True)
    ngaythi = fields.Date('Exam Date', required=False)