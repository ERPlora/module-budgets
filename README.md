# Budgets Module

Budget planning, tracking and variance analysis.

## Features

- Create and manage budgets with defined periods (start/end dates)
- Track total budget amounts and spent amounts per budget
- Break down budgets into categorized line items with planned vs. actual amounts
- Monitor budget status (active, closed, etc.)
- Dashboard overview of all budgets
- Variance analysis between planned and actual spending

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Budgets > Settings**

## Usage

Access via: **Menu > Budgets**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/budgets/dashboard/` | Overview of budget status and key metrics |
| Budgets | `/m/budgets/budgets/` | List, create and manage budgets |
| Settings | `/m/budgets/settings/` | Module configuration |

## Models

| Model | Description |
|-------|-------------|
| `Budget` | A budget with name, period (start/end dates), total amount, spent amount, status, and notes |
| `BudgetLine` | Individual line item within a budget, tracking category, planned amount, and actual amount |

## Permissions

| Permission | Description |
|------------|-------------|
| `budgets.view_budget` | View budgets |
| `budgets.add_budget` | Create new budgets |
| `budgets.change_budget` | Edit existing budgets |
| `budgets.delete_budget` | Delete budgets |
| `budgets.manage_settings` | Manage module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
