    from django.utils.translation import gettext_lazy as _

    MODULE_ID = 'budgets'
    MODULE_NAME = _('Budgets')
    MODULE_VERSION = '1.0.0'
    MODULE_ICON = 'pie-chart-outline'
    MODULE_DESCRIPTION = _('Budget planning, tracking and variance analysis')
    MODULE_AUTHOR = 'ERPlora'
    MODULE_CATEGORY = 'finance'

    MENU = {
        'label': _('Budgets'),
        'icon': 'pie-chart-outline',
        'order': 48,
    }

    NAVIGATION = [
        {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Budgets'), 'icon': 'pie-chart-outline', 'id': 'budgets'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
    ]

    DEPENDENCIES = []

    PERMISSIONS = [
        'budgets.view_budget',
'budgets.add_budget',
'budgets.change_budget',
'budgets.delete_budget',
'budgets.manage_settings',
    ]
