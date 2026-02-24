from django.urls import path
from . import views

app_name = 'budgets'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Budget
    path('budgets/', views.budgets_list, name='budgets_list'),
    path('budgets/add/', views.budget_add, name='budget_add'),
    path('budgets/<uuid:pk>/edit/', views.budget_edit, name='budget_edit'),
    path('budgets/<uuid:pk>/delete/', views.budget_delete, name='budget_delete'),
    path('budgets/bulk/', views.budgets_bulk_action, name='budgets_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
