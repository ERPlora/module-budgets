"""
Budgets Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('budgets', 'dashboard')
@htmx_view('budgets/pages/dashboard.html', 'budgets/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('budgets', 'budgets')
@htmx_view('budgets/pages/budgets.html', 'budgets/partials/budgets_content.html')
def budgets(request):
    """Budgets view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('budgets', 'settings')
@htmx_view('budgets/pages/settings.html', 'budgets/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

