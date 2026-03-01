# ALX Django Capstone Project - Library Management System API

## Project Description
This project is a **Library Management System API** built with Django and Django REST Framework.  
It allows users to:
- Register and login
- View, add, update, and delete books
- Borrow (checkout) and return books
- View all users (admin only)
- Use token-based authentication for secure API access

---

## Features

### Accounts
- `POST /api/accounts/register/` – Register a new user
- `POST /api/accounts/login/` – Login and get an authentication token

### Books
- `GET /api/books/` – List all books
- `POST /api/books/` – Add a new book (admin only)
- `GET /api/books/<id>/` – Retrieve book details
- `PUT /api/books/<id>/` – Update book details (admin only)
- `DELETE /api/books/<id>/` – Delete book (admin only)

### Borrow/Return
- `POST /api/checkout/` – Borrow a book
- `POST /api/return/` – Return a borrowed book

### Users
- `GET /api/users/` – List all users (admin only)
- `POST /api/users/` – Add a new user (admin only)

---

## Authentication
- Token-based authentication is required for most endpoints.
- Include in headers:
  Authorization: Token <your_token_here>

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repo-url>
cd ALX_Django_Project

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

## Testing
Use the provided Postman collection to test all API endpoints in the correct order.