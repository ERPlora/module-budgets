"""Tests for budgets models."""
import pytest
from django.utils import timezone

from budgets.models import Budget


@pytest.mark.django_db
class TestBudget:
    """Budget model tests."""

    def test_create(self, budget):
        """Test Budget creation."""
        assert budget.pk is not None
        assert budget.is_deleted is False

    def test_str(self, budget):
        """Test string representation."""
        assert str(budget) is not None
        assert len(str(budget)) > 0

    def test_soft_delete(self, budget):
        """Test soft delete."""
        pk = budget.pk
        budget.is_deleted = True
        budget.deleted_at = timezone.now()
        budget.save()
        assert not Budget.objects.filter(pk=pk).exists()
        assert Budget.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, budget):
        """Test default queryset excludes deleted."""
        budget.is_deleted = True
        budget.deleted_at = timezone.now()
        budget.save()
        assert Budget.objects.filter(hub_id=hub_id).count() == 0


