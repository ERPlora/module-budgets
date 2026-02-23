from django.urls import path
from . import views

app_name = 'budgets'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('budgets/', views.budgets, name='budgets'),
    path('settings/', views.settings, name='settings'),
]
