# -*- coding: utf-8 -*-
{
    'name': "My pet - Duyen.info",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'author': "Duyen.info",
    'website': "https://duyenng.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': -100,
    'depends': [
        'product', 'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
