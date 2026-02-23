from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BudgetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'budgets'
    label = 'budgets'
    verbose_name = _('Budgets')

    def ready(self):
        pass
