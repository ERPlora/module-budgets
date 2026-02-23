from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

class Budget(HubBaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    period_start = models.DateField(verbose_name=_('Period Start'))
    period_end = models.DateField(verbose_name=_('Period End'))
    total_amount = models.DecimalField(max_digits=14, decimal_places=2, default='0', verbose_name=_('Total Amount'))
    spent_amount = models.DecimalField(max_digits=14, decimal_places=2, default='0', verbose_name=_('Spent Amount'))
    status = models.CharField(max_length=20, default='active', verbose_name=_('Status'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta(HubBaseModel.Meta):
        db_table = 'budgets_budget'

    def __str__(self):
        return self.name


class BudgetLine(HubBaseModel):
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE, related_name='lines')
    category = models.CharField(max_length=100, verbose_name=_('Category'))
    planned_amount = models.DecimalField(max_digits=14, decimal_places=2, default='0', verbose_name=_('Planned Amount'))
    actual_amount = models.DecimalField(max_digits=14, decimal_places=2, default='0', verbose_name=_('Actual Amount'))

    class Meta(HubBaseModel.Meta):
        db_table = 'budgets_budgetline'

    def __str__(self):
        return str(self.id)

