# Django REST Framework Backend - Setup Guide

## Project Structure

```
backend/
├── config/              # Django settings and URLs
│   ├── settings.py     # Main settings file
│   ├── urls.py         # Root URL configuration
│   └── __init__.py
├── apps/
│   ├── core/           # Base models and utilities
│   ├── auth_app/       # Authentication and JWT
│   ├── employee/       # Employee, Attendance, Advances
│   ├── bill/           # Bills management
│   ├── order/          # Orders management
│   ├── dealer/         # Dealers management
│   ├── transaction/    # Transactions and Categories
│   ├── inventory/      # Inventory management
│   └── attendance/     # Attendance endpoints
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Setup Instructions

### 1. Create Virtual Environment
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Seed Data
```bash
python manage.py seed_categories    # Seed transaction types and categories
python manage.py seed_users         # Create test users
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run Server
```bash
python manage.py runserver 0.0.0.0:3000
```

## API Endpoints

### Authentication
- `POST /api/auth/login/` - Login with username and password
- `POST /api/auth/register/` - Register new user
- `GET /api/auth/me/` - Get current user (requires token)

### Employees
- `GET /api/employees/` - List all employees
- `POST /api/employees/` - Create employee
- `GET /api/employees/{id}/` - Get employee details
- `PUT /api/employees/{id}/` - Update employee
- `DELETE /api/employees/{id}/` - Delete employee

### Attendance
- `GET /api/employees/{employee_id}/attendance/` - Get attendance records
- `POST /api/employees/{employee_id}/attendance/` - Mark attendance

### Advances
- `GET /api/employees/{employee_id}/advances/` - Get employee advances
- `POST /api/employees/{employee_id}/advances/` - Create advance

### Bills
- `GET /api/bills/` - List all bills
- `POST /api/bills/` - Create bill
- `GET /api/bills/{id}/` - Get bill details
- `PUT /api/bills/{id}/` - Update bill
- `DELETE /api/bills/{id}/` - Delete bill

### Orders
- `GET /api/orders/` - List all orders
- `POST /api/orders/` - Create order
- `GET /api/orders/{id}/` - Get order details
- `PUT /api/orders/{id}/` - Update order
- `DELETE /api/orders/{id}/` - Delete order

### Dealers
- `GET /api/dealers/` - List all dealers
- `POST /api/dealers/` - Create dealer
- `GET /api/dealers/{id}/` - Get dealer details
- `PUT /api/dealers/{id}/` - Update dealer
- `DELETE /api/dealers/{id}/` - Delete dealer

### Transactions
- `GET /api/transactions/` - List all transactions
- `POST /api/transactions/` - Create transaction
- `GET /api/transactions/{id}/` - Get transaction details
- `PUT /api/transactions/{id}/` - Update transaction
- `DELETE /api/transactions/{id}/` - Delete transaction
- `GET /api/transactions/by-type/?type=Sales` - Get transactions by type

### Transaction Types
- `GET /api/transactions/types/` - List all transaction types
- `GET /api/transactions/types/with-categories/` - Get types with categories
- `GET /api/transactions/types/by-name/{name}/` - Get type by name with categories

### Categories
- `GET /api/transactions/income-categories/` - List income categories
- `GET /api/transactions/expense-categories/` - List expense categories

### Inventory
- `GET /api/inventory/` - List inventory items
- `POST /api/inventory/` - Create inventory item
- `GET /api/inventory/{id}/` - Get inventory details
- `PUT /api/inventory/{id}/` - Update inventory
- `DELETE /api/inventory/{id}/` - Delete inventory
- `GET /api/inventory/low-stock/` - Get low stock items

## Test Users

After running seed_users command:
- Owner: `username: owner` / `password: owner123`
- Manager: `username: manager` / `password: manager123`

## Database

The system uses SQLite database stored at the project root as `dev.db`.

## Authentication

All endpoints (except login/register) require JWT token in the Authorization header:
```
Authorization: Bearer {token}
```

## Roles

- **Owner**: View-only access
- **Manager**: Full CRUD access
