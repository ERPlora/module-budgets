"""
Budgets Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import Budget, BudgetLine

PER_PAGE_CHOICES = [10, 25, 50, 100]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('budgets', 'dashboard')
@htmx_view('budgets/pages/index.html', 'budgets/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_budgets': Budget.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# Budget
# ======================================================================

BUDGET_SORT_FIELDS = {
    'name': 'name',
    'status': 'status',
    'spent_amount': 'spent_amount',
    'total_amount': 'total_amount',
    'period_start': 'period_start',
    'period_end': 'period_end',
    'created_at': 'created_at',
}

def _build_budgets_context(hub_id, per_page=10):
    qs = Budget.objects.filter(hub_id=hub_id, is_deleted=False).order_by('name')
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(1)
    return {
        'budgets': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'name',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_budgets_list(request, hub_id, per_page=10):
    ctx = _build_budgets_context(hub_id, per_page)
    return django_render(request, 'budgets/partials/budgets_list.html', ctx)

@login_required
@with_module_nav('budgets', 'budgets')
@htmx_view('budgets/pages/budgets.html', 'budgets/partials/budgets_content.html')
def budgets_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'name')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 10

    qs = Budget.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(name__icontains=search_query) | Q(status__icontains=search_query) | Q(notes__icontains=search_query))

    order_by = BUDGET_SORT_FIELDS.get(sort_field, 'name')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['name', 'status', 'spent_amount', 'total_amount', 'period_start', 'period_end']
        headers = ['Name', 'Status', 'Spent Amount', 'Total Amount', 'Period Start', 'Period End']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='budgets.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='budgets.xlsx')

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'budgets/partials/budgets_list.html', {
            'budgets': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'budgets': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
def budget_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        period_start = request.POST.get('period_start') or None
        period_end = request.POST.get('period_end') or None
        total_amount = request.POST.get('total_amount', '0') or '0'
        spent_amount = request.POST.get('spent_amount', '0') or '0'
        status = request.POST.get('status', '').strip()
        notes = request.POST.get('notes', '').strip()
        obj = Budget(hub_id=hub_id)
        obj.name = name
        obj.period_start = period_start
        obj.period_end = period_end
        obj.total_amount = total_amount
        obj.spent_amount = spent_amount
        obj.status = status
        obj.notes = notes
        obj.save()
        return _render_budgets_list(request, hub_id)
    return django_render(request, 'budgets/partials/panel_budget_add.html', {})

@login_required
def budget_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Budget, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '').strip()
        obj.period_start = request.POST.get('period_start') or None
        obj.period_end = request.POST.get('period_end') or None
        obj.total_amount = request.POST.get('total_amount', '0') or '0'
        obj.spent_amount = request.POST.get('spent_amount', '0') or '0'
        obj.status = request.POST.get('status', '').strip()
        obj.notes = request.POST.get('notes', '').strip()
        obj.save()
        return _render_budgets_list(request, hub_id)
    return django_render(request, 'budgets/partials/panel_budget_edit.html', {'obj': obj})

@login_required
@require_POST
def budget_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Budget, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_budgets_list(request, hub_id)

@login_required
@require_POST
def budgets_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = Budget.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_budgets_list(request, hub_id)


@login_required
@with_module_nav('budgets', 'settings')
@htmx_view('budgets/pages/settings.html', 'budgets/partials/settings_content.html')
def settings_view(request):
    return {}

