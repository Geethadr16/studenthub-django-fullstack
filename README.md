
# StudentHub — Student Management System

A web-based Student Management System developed using Python and Django. StudentHub provides a responsive dashboard for managing student records, with CRUD operations, database-wide search, sorting, pagination, and automated testing.

## Features

- **Student Management:** Add, view, update, and delete student records.
- **Search:** Search students by name, email, or place using Django ORM queries.
- **Sorting:** Sort records by name, age, and date of birth.
- **Pagination:** Display five student records per page.
- **Dashboard Statistics:** View total students, matching records, and records displayed.
- **Delete Confirmation:** Require confirmation before deleting a student.
- **Responsive Interface:** Bootstrap-based dashboard with reusable Django templates.
- **Automated Testing:** Django unit tests covering CRUD operations, search, sorting, and pagination.

## Tech Stack

- **Backend:** Python, Django 5.2.7
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite
- **Version Control:** Git and GitHub
- **Testing:** Django TestCase

## Project Structure

```text
fvbcrudproject/
├── fvbcrudproject/       # Django project configuration
├── myapp/                # Models, forms, views and tests
├── templates/
│   └── myapp/            # Reusable HTML templates
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Geethadr16/studenthub.git
cd studenthub
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment (Windows)

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file containing a Django secret key:

```env
DJANGO_SECRET_KEY=replace-with-your-own-secret-key
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/

## Automated Testing

Run the Django test suite:

```bash
python manage.py test myapp
```

The project includes 11 automated tests covering student models, CRUD views, search, sorting, and pagination.

## Screenshots

Dashboard and application screenshots will be added here.

## Future Improvements

- Student record validation enhancements
- Authentication and role-based access control
- Cloud deployment
- CI/CD automation using GitHub Actions

## Author

Geetha D R

GitHub: https://github.com/Geethadr16
