###############################################################################
# Author: SINAPSYS GLOBAL SA || MASTERCORE SAS
# Copyleft: 2020-Present.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
#
###############################################################################
{
    'name': "Localización Withholding Venezuela",
    'description': """
        **Localización VENEZUELA Withholding**

        ¡Felicidades!. Este es el módulo Withholding para la implementación de 
        la **Localización Venezuela** que agrega características y datos 
        necesarios para un correcto ejercicio fiscal de su empresa.
    """,

    'author': "SINAPSYS GLOBAL SA || MASTERCORE SAS",
    'website': "http://sinapsys.global",
    'version': '13.0.1',
    'category': 'Localization',
    'license': 'AGPL-3',
    'depends': ['account',],
    'data': [
        'views/account_payment_group_view.xml',
        'views/account_payment_view.xml',
        'views/account_tax_view.xml',
        'views/res_partner_view.xml',
        'wizards/res_config_settings_views.xml',
        'security/ir.model.access.csv',
        'data/account_payment_method_data.xml',
    ],

}
