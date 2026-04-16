from django.core.management.base import BaseCommand
from apps.transaction.models import TransactionType, IncomeCategory, ExpenseCategory


class Command(BaseCommand):
    help = "Seed transaction types and categories"

    def handle(self, *args, **options):
        # Define transaction types and their categories
        categories_data = {
            "Sales": {
                "description": "Sales transactions",
                "income": [
                    "Online Sales",
                    "Physical Store Sales",
                    "Dealer Orders",
                    "Wholesale",
                    "Bulk Orders",
                ],
                "expense": [],
            },
            "Asset": {
                "description": "Asset purchases",
                "income": [],
                "expense": [
                    "Equipment Purchase",
                    "Furniture & Fixtures",
                    "Vehicles",
                    "Computer & IT Equipment",
                    "Building/Property",
                ],
            },
            "Capital": {
                "description": "Capital transactions",
                "income": [
                    "Loan Repayment",
                    "Owner Capital Contribution",
                    "Retained Earnings",
                    "Debt Financing",
                    "Equity Investment",
                ],
                "expense": [],
            },
            "Salary": {
                "description": "Salary and payroll",
                "income": [],
                "expense": [
                    "Salary & Wages",
                    "Bonus & Incentives",
                    "Benefits & Allowances",
                    "Payroll Taxes",
                    "Employee Benefits",
                ],
            },
            "Operating": {
                "description": "Operating expenses",
                "income": [],
                "expense": [
                    "Rent",
                    "Utilities",
                    "Transportation",
                    "Maintenance",
                    "Office Supplies",
                    "Insurance",
                    "Bank Charges",
                ],
            },
            "Material": {
                "description": "Material purchases",
                "income": [],
                "expense": [
                    "Raw Materials",
                    "Fabric & Textiles",
                    "Packaging Materials",
                    "Dyeing & Chemicals",
                    "Inventory Stock",
                ],
            },
            "Other Income": {
                "description": "Other income sources",
                "income": [
                    "Interest Income",
                    "Returns & Refunds Recovered",
                    "Miscellaneous Income",
                    "Rental Income",
                ],
                "expense": [],
            },
            "Other Expense": {
                "description": "Other expenses",
                "income": [],
                "expense": [
                    "Miscellaneous Expense",
                    "Contingency Fund",
                    "Repairs & Maintenance",
                    "Professional Fees",
                    "Donations",
                ],
            },
        }

        for type_name, data in categories_data.items():
            tx_type, created = TransactionType.objects.get_or_create(
                name=type_name,
                defaults={"description": data["description"]},
            )

            if created:
                self.stdout.write(f"Created transaction type: {type_name}")

            # Create income categories
            for category_name in data["income"]:
                IncomeCategory.objects.get_or_create(
                    name=category_name,
                    transaction_type=tx_type,
                    defaults={"description": f"{category_name} for {type_name}"},
                )
                self.stdout.write(f"  Created income category: {category_name}")

            # Create expense categories
            for category_name in data["expense"]:
                ExpenseCategory.objects.get_or_create(
                    name=category_name,
                    transaction_type=tx_type,
                    defaults={"description": f"{category_name} for {type_name}"},
                )
                self.stdout.write(f"  Created expense category: {category_name}")

        self.stdout.write(self.style.SUCCESS("Successfully seeded transaction types and categories"))
