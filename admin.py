from django.contrib import admin

from .models import Budget, BudgetLine

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['name', 'period_start', 'period_end', 'total_amount', 'spent_amount', 'created_at']
    search_fields = ['name', 'status', 'notes']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(BudgetLine)
class BudgetLineAdmin(admin.ModelAdmin):
    list_display = ['budget', 'category', 'planned_amount', 'actual_amount', 'created_at']
    search_fields = ['category']
    readonly_fields = ['created_at', 'updated_at']

