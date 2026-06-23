HR Management System (Gestão RH)

A robust Human Resources Management System built with Django and Python. This project is designed to streamline HR processes, including employee data management, document handling, and organizational structure tracking.

🚀 Technologies Used

•
Backend: Django (Python)

•
Database: PostgreSQL (Production) / SQLite (Development)

•
Frontend: HTML5, CSS3, JavaScript (Django Templates)

•
Architecture: Model-View-Template (MVT)

•
Asset Management: Configured for static and media file handling (Nginx/WhiteNoise ready).

✨ Key Features

•
Employee Management: Create, read, update, and delete (CRUD) employee profiles.

•
Organizational Structure: Manage departments, divisions, and roles within the company.

•
Document Management: Secure storage and retrieval of employee-related documents.

•
Authentication & Authorization: Secure login system with role-based access control (RBAC).

•
Admin Dashboard: Leveraging Django's powerful admin interface for rapid data management.

🛠️ Getting Started

To get a local copy up and running, follow these simple steps:

Prerequisites

•
Python 3.x

•
pip (Python package manager)

•
Virtualenv (recommended)

Installation

1.
Clone the repository:

Bash


git clone https://github.com/devgabrielcd/gestao_rh.git





2.
Navigate to the project directory:

Bash


cd gestao_rh





3.
Create and activate a virtual environment:

Bash


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate





4.
Install dependencies:

Bash


pip install -r requirements.txt





5.
Run migrations:

Bash


python manage.py migrate





6.
Start the development server:

Bash


python manage.py runserver





7.
Access the application at http://127.0.0.1:8000.

👤 Author

Gabriel Dechiara

•
LinkedIn: gabriel-dechiara

•
GitHub: @devgabrielcd




This project demonstrates the application of Django for building scalable and secure enterprise-level management systems.

