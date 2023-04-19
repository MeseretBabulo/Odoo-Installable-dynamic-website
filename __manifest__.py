# -*- coding: utf-8 -*-
# Copyright 2016, 2020 Openworx - Mario Gielissen
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "AADBO Webiste",
    "summary": "",
    "version": "13.0.0.3",
    "category": "",
    "website": "",
	"description": """
    Installable Odoo Dynamic website
    """,
	'images':[
        'images/f.png'
	],
    "author": "mesi2640@gmail.com",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["website"   
    ],
    "data": [
        'views/view.xml',
		'views/template.xml',
		
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
