# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'School Management Software',
    'sequence': -100,
    'description': """School Management Software""",
    'category': 'Services',
    'website': 'https://www.odoo.school',
    'license': 'LGPL-3',
    'depends': [
        'hr'
    ],
    'data': [
        'data/data.xml',
        'views/department.xml',
        'views/lecturer.xml',
        'views/student.xml',
        'views/ology.xml',
        # 'views/course.xml',
        'views/classroom.xml',
        'views/major.xml',
        'views/school.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}