from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Budget

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'period_start', 'period_end', 'total_amount', 'spent_amount', 'status', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'period_start': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'period_end': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'total_amount': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'spent_amount': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'status': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'notes': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
        }

