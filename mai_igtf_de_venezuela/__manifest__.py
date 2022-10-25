{
    'name': "IGTF workflow | Backend IGTF | IGTF de Venezuela",
    "version": "14.1.1.1",
    "description": """
        Using this module you can add IGTF for Venezuela.
    """,
    "summary": """Using this module you can add IGTF for Venezuela.""",
    'category': 'Sales',
    'price': 99,
    'currency': 'USD',
    'license': 'OPL-1',
    "author" : "MAISOLUTIONSLLC",
    'sequence': 1,
    "email": 'apps@maisolutionsllc.com',
    "website":'http://maisolutionsllc.com/',
    "depends" : ['base', 'sale', 'sale_management', 'account'],
	"data": [
        'views/res_company_view.xml',
	],
    "images": ['static/description/main_screenshot.png'],
    "live_test_url" : "",
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
