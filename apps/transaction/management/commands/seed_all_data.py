from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.auth_app.models import UserProfile
from apps.employee.models import Employee, Attendance, EmployeeAdvance
from apps.inventory.models import Inventory
from apps.order.models import Order
from apps.bill.models import Bill
from apps.dealer.models import Dealer
from apps.transaction.models import Transaction, TransactionType, IncomeCategory, ExpenseCategory
from decimal import Decimal
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = "Seed all dummy data for the garment management system"

    def handle(self, *args, **options):
        self.stdout.write("Starting data seeding...")

        # Seed Employees
        self.seed_employees()

        # Seed Inventory
        self.seed_inventory()

        # Seed Dealers
        self.seed_dealers()

        # Seed Bills
        self.seed_bills()

        # Seed Orders
        self.seed_orders()

        # Seed Attendance
        self.seed_attendance()

        # Seed Employee Advances
        self.seed_advances()

        # Seed Transactions
        self.seed_transactions()

        self.stdout.write(self.style.SUCCESS("✓ All data seeded successfully!"))

    def seed_employees(self):
        self.stdout.write("Seeding employees...")
        employees_data = [
            {
                "name": "Rajesh Kumar",
                "role": "Floor Manager",
                "department": "Production",
                "phone": "+91 98765 43210",
                "salary": 45000,
                "join_date": "2022-03-15",
            },
            {
                "name": "Priya Sharma",
                "role": "Tailor",
                "department": "Production",
                "phone": "+91 98765 43211",
                "salary": 28000,
                "join_date": "2023-01-10",
            },
            {
                "name": "Amit Patel",
                "role": "Quality Inspector",
                "department": "Quality",
                "phone": "+91 98765 43212",
                "salary": 32000,
                "join_date": "2022-07-20",
            },
            {
                "name": "Sunita Devi",
                "role": "Cutting Operator",
                "department": "Production",
                "phone": "+91 98765 43213",
                "salary": 25000,
                "join_date": "2023-06-01",
            },
            {
                "name": "Mohammad Irfan",
                "role": "Warehouse Head",
                "department": "Logistics",
                "phone": "+91 98765 43214",
                "salary": 38000,
                "join_date": "2021-11-05",
            },
            {
                "name": "Kavita Singh",
                "role": "Accountant",
                "department": "Finance",
                "phone": "+91 98765 43215",
                "salary": 35000,
                "join_date": "2022-09-12",
            },
            {
                "name": "Ravi Verma",
                "role": "Sales Executive",
                "department": "Sales",
                "phone": "+91 98765 43216",
                "salary": 30000,
                "join_date": "2023-04-18",
            },
            {
                "name": "Anita Gupta",
                "role": "Designer",
                "department": "Design",
                "phone": "+91 98765 43217",
                "salary": 42000,
                "join_date": "2022-02-28",
            },
        ]

        for data in employees_data:
            emp, created = Employee.objects.get_or_create(
                phone=data["phone"],
                defaults={
                    "name": data["name"],
                    "role": data["role"],
                    "department": data["department"],
                    "salary": Decimal(str(data["salary"])),
                    "join_date": data["join_date"],
                    "status": "active",
                },
            )
            if created:
                self.stdout.write(f"  Created employee: {data['name']}")

    def seed_inventory(self):
        self.stdout.write("Seeding inventory...")
        inventory_data = [
            {
                "item_name": "Cotton Fabric (White)",
                "category": "fabric",
                "sku": "FAB-COT-W01",
                "quantity": 450,
                "unit": "meters",
                "unit_price": Decimal("120"),
                "min_stock": 100,
                "supplier": "Arvind Mills",
            },
            {
                "item_name": "Silk Fabric (Red)",
                "category": "fabric",
                "sku": "FAB-SLK-R01",
                "quantity": 80,
                "unit": "meters",
                "unit_price": Decimal("650"),
                "min_stock": 50,
                "supplier": "Mysore Silk Co",
            },
            {
                "item_name": "Men's Formal Shirt",
                "category": "garment",
                "sku": "GAR-MFS-001",
                "quantity": 320,
                "unit": "pcs",
                "unit_price": Decimal("850"),
                "min_stock": 50,
                "supplier": "In-house",
            },
            {
                "item_name": "Women's Kurti",
                "category": "garment",
                "sku": "GAR-WKU-001",
                "quantity": 180,
                "unit": "pcs",
                "unit_price": Decimal("1200"),
                "min_stock": 30,
                "supplier": "In-house",
            },
            {
                "item_name": "Buttons (Pearl)",
                "category": "accessory",
                "sku": "ACC-BTN-P01",
                "quantity": 5000,
                "unit": "pcs",
                "unit_price": Decimal("5"),
                "min_stock": 1000,
                "supplier": "Button World",
            },
            {
                "item_name": "Zipper (Metal 7inch)",
                "category": "accessory",
                "sku": "ACC-ZIP-M07",
                "quantity": 1200,
                "unit": "pcs",
                "unit_price": Decimal("15"),
                "min_stock": 300,
                "supplier": "YKK India",
            },
            {
                "item_name": "Thread (Black)",
                "category": "raw_material",
                "sku": "RAW-THR-B01",
                "quantity": 200,
                "unit": "spools",
                "unit_price": Decimal("45"),
                "min_stock": 50,
                "supplier": "Coats India",
            },
            {
                "item_name": "Denim Fabric (Blue)",
                "category": "fabric",
                "sku": "FAB-DEN-B01",
                "quantity": 30,
                "unit": "meters",
                "unit_price": Decimal("280"),
                "min_stock": 100,
                "supplier": "Arvind Mills",
            },
            {
                "item_name": "Packaging Boxes (L)",
                "category": "raw_material",
                "sku": "RAW-PKG-L01",
                "quantity": 600,
                "unit": "pcs",
                "unit_price": Decimal("25"),
                "min_stock": 200,
                "supplier": "Pack Solutions",
            },
        ]

        for data in inventory_data:
            inv, created = Inventory.objects.get_or_create(
                sku=data["sku"],
                defaults=data,
            )
            if created:
                self.stdout.write(f"  Created inventory: {data['item_name']}")

    def seed_dealers(self):
        self.stdout.write("Seeding dealers...")
        dealers_data = [
            {
                "name": "Suresh Agarwal (Textile Hub Dealers)",
                "phone": "+91 99887 76655",
                "email": "suresh@textilehub.com",
                "dealer_type": "buyer",
                "address": "North India",
            },
            {
                "name": "Manoj Reddy (Fashion Point Dealers)",
                "phone": "+91 99887 76656",
                "email": "manoj@fashionpoint.com",
                "dealer_type": "buyer",
                "address": "South India",
            },
            {
                "name": "Vikram Joshi (Garment Galaxy)",
                "phone": "+91 99887 76657",
                "email": "vikram@garmentgalaxy.com",
                "dealer_type": "buyer",
                "address": "West India",
            },
            {
                "name": "Rahul Mehta (Style Street)",
                "phone": "+91 99887 76658",
                "email": "rahul@stylestreet.com",
                "dealer_type": "buyer",
                "address": "East India",
            },
            {
                "name": "Deepak Bansal (Trendy Textiles)",
                "phone": "+91 99887 76659",
                "email": "deepak@trendytex.com",
                "dealer_type": "buyer",
                "address": "Central India",
            },
        ]

        for data in dealers_data:
            dealer, created = Dealer.objects.get_or_create(
                phone=data["phone"],
                defaults=data,
            )
            if created:
                self.stdout.write(f"  Created dealer: {data['name']}")

    def seed_bills(self):
        self.stdout.write("Seeding bills...")
        bills_data = [
            {
                "vendor_id": "Arvind Mills",
                "amount": Decimal("54000"),
                "bill_date": "2026-02-02",
                "due_date": "2026-03-02",
                "status": "paid",
                "description": "Cotton Fabric Purchase",
            },
            {
                "vendor_id": "YKK India",
                "amount": Decimal("18000"),
                "bill_date": "2026-02-12",
                "due_date": "2026-03-10",
                "status": "unpaid",
                "description": "Metal Zippers Purchase",
            },
            {
                "vendor_id": "State Electricity Board",
                "amount": Decimal("18500"),
                "bill_date": "2026-02-07",
                "due_date": "2026-02-28",
                "status": "paid",
                "description": "Factory Electricity Bill",
            },
            {
                "vendor_id": "Coats India",
                "amount": Decimal("9000"),
                "bill_date": "2026-02-14",
                "due_date": "2026-03-14",
                "status": "unpaid",
                "description": "Thread Spools Purchase",
            },
            {
                "vendor_id": "Pack Solutions",
                "amount": Decimal("15000"),
                "bill_date": "2026-02-01",
                "due_date": "2026-02-20",
                "status": "overdue",
                "description": "Packaging Boxes Purchase",
            },
            {
                "vendor_id": "Mysore Silk Co",
                "amount": Decimal("52000"),
                "bill_date": "2026-02-15",
                "due_date": "2026-03-15",
                "status": "unpaid",
                "description": "Silk Fabric Purchase",
            },
        ]

        for data in bills_data:
            bill, created = Bill.objects.get_or_create(
                vendor_id=data["vendor_id"],
                bill_date=data["bill_date"],
                defaults={k: v for k, v in data.items() if k not in ["vendor_id", "bill_date"]},
            )
            if created:
                self.stdout.write(f"  Created bill: {data['vendor_id']}")

    def seed_orders(self):
        self.stdout.write("Seeding orders...")
        orders_data = [
            {
                "order_number": "ORD-2026-001",
                "customer_name": "Flipkart Marketplace",
                "customer_type": "company",
                "total_amount": Decimal("65000"),
                "status": "delivered",
                "order_date": "2026-02-01",
            },
            {
                "order_number": "ORD-2026-002",
                "customer_name": "Walk-in Customer",
                "customer_type": "individual",
                "total_amount": Decimal("3600"),
                "status": "delivered",
                "order_date": "2026-02-05",
            },
            {
                "order_number": "ORD-2026-003",
                "customer_name": "Textile Hub Dealers",
                "customer_type": "company",
                "total_amount": Decimal("455000"),
                "status": "processing",
                "order_date": "2026-02-10",
            },
            {
                "order_number": "ORD-2026-004",
                "customer_name": "Amazon India",
                "customer_type": "company",
                "total_amount": Decimal("136000"),
                "status": "shipped",
                "order_date": "2026-02-12",
            },
            {
                "order_number": "ORD-2026-005",
                "customer_name": "Retail Store - MG Road",
                "customer_type": "company",
                "total_amount": Decimal("16500"),
                "status": "pending",
                "order_date": "2026-02-18",
            },
            {
                "order_number": "ORD-2026-006",
                "customer_name": "Fashion Point Dealers",
                "customer_type": "company",
                "total_amount": Decimal("156000"),
                "status": "pending",
                "order_date": "2026-02-19",
            },
            {
                "order_number": "ORD-2026-007",
                "customer_name": "Myntra",
                "customer_type": "company",
                "total_amount": Decimal("52500"),
                "status": "processing",
                "order_date": "2026-02-20",
            },
        ]

        for data in orders_data:
            order, created = Order.objects.get_or_create(
                order_number=data["order_number"],
                defaults=data,
            )
            if created:
                self.stdout.write(f"  Created order: {data['order_number']}")

    def seed_attendance(self):
        self.stdout.write("Seeding attendance...")
        # Get first 2 employees
        employees = Employee.objects.all()[:2]
        dates = [
            ("2026-02-20", "present"),
            ("2026-02-19", "present"),
        ]

        for emp in employees:
            for date_str, status in dates:
                attendance, created = Attendance.objects.get_or_create(
                    employee=emp,
                    date=date_str,
                    defaults={"status": status},
                )
                if created:
                    self.stdout.write(f"  Created attendance: {emp.name} - {date_str}")

    def seed_advances(self):
        self.stdout.write("Seeding employee advances...")
        advances_data = [
            {
                "employee_name": "Rajesh Kumar",
                "amount": Decimal("5000"),
                "date": "2026-02-10",
                "notes": "Personal need",
            },
            {
                "employee_name": "Priya Sharma",
                "amount": Decimal("3000"),
                "date": "2026-02-15",
                "notes": "Medical expense",
            },
        ]

        for data in advances_data:
            try:
                employee = Employee.objects.get(name=data["employee_name"])
                advance, created = EmployeeAdvance.objects.get_or_create(
                    employee=employee,
                    date=data["date"],
                    defaults={
                        "amount": data["amount"],
                        "notes": data["notes"],
                        "status": "pending",
                    },
                )
                if created:
                    self.stdout.write(f"  Created advance: {data['employee_name']}")
            except Employee.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(
                        f"  Employee {data['employee_name']} not found"
                    )
                )

    def seed_transactions(self):
        self.stdout.write("Seeding transactions...")
        transactions_data = [
            {
                "type": "income",
                "category": "Online Sales",
                "description": "Flipkart order payment",
                "amount": Decimal("65000"),
                "date": "2026-02-03",
                "reference": "ORD-2026-001",
            },
            {
                "type": "income",
                "category": "Physical Store Sales",
                "description": "Counter sale",
                "amount": Decimal("3600"),
                "date": "2026-02-05",
                "reference": None,
            },
            {
                "type": "expense",
                "category": "Raw Materials",
                "description": "Cotton fabric purchase from Arvind Mills",
                "amount": Decimal("54000"),
                "date": "2026-02-02",
                "reference": None,
            },
            {
                "type": "expense",
                "category": "Salary & Wages",
                "description": "February salaries payout",
                "amount": Decimal("275000"),
                "date": "2026-02-01",
                "reference": None,
            },
            {
                "type": "expense",
                "category": "Utilities",
                "description": "Factory electricity bill",
                "amount": Decimal("18500"),
                "date": "2026-02-07",
                "reference": None,
            },
            {
                "type": "income",
                "category": "Wholesale",
                "description": "Advance from Textile Hub",
                "amount": Decimal("200000"),
                "date": "2026-02-11",
                "reference": "ORD-2026-003",
            },
            {
                "type": "expense",
                "category": "Transportation",
                "description": "Shipping charges for Amazon order",
                "amount": Decimal("8500"),
                "date": "2026-02-13",
                "reference": None,
            },
            {
                "type": "income",
                "category": "Online Sales",
                "description": "Amazon order payment",
                "amount": Decimal("136000"),
                "date": "2026-02-15",
                "reference": "ORD-2026-004",
            },
            {
                "type": "expense",
                "category": "Maintenance",
                "description": "Sewing machine repair",
                "amount": Decimal("12000"),
                "date": "2026-02-16",
                "reference": None,
            },
            {
                "type": "expense",
                "category": "Packaging Materials",
                "description": "Packaging material purchase",
                "amount": Decimal("15000"),
                "date": "2026-02-14",
                "reference": None,
            },
            {
                "type": "income",
                "category": "Physical Store Sales",
                "description": "Bulk walk-in purchase",
                "amount": Decimal("28000"),
                "date": "2026-02-17",
                "reference": None,
            },
        ]

        for data in transactions_data:
            transaction, created = Transaction.objects.get_or_create(
                description=data["description"],
                date=data["date"],
                defaults={k: v for k, v in data.items() if k not in ["description", "date"]},
            )
            if created:
                self.stdout.write(f"  Created transaction: {data['description']}")
