# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Quản lý bệnh viện',
    'version' : '1.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoo.hospital',
    'license': 'LGPL-3',
    'depends' : [],
    'data': [
        'views/bnviews.xml',
        'data/data_pt.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}