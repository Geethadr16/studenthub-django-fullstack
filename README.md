# StudentHub — Student Management System

A full-stack Student Management System built using **Python, Django, SQLite, HTML, CSS, Bootstrap, and JavaScript**. StudentHub provides a responsive dashboard for managing student records through CRUD operations, database search, sorting, pagination, and dashboard statistics.

The application includes automated testing using Django's testing framework and is deployed on PythonAnywhere for public access.

## Live Demo

**Live Application:** https://geethadr.pythonanywhere.com/

**GitHub Repository:** https://github.com/Geethadr16/studenthub-django-fullstack

**Deployment Platform:** PythonAnywhere

## Features

- **Student Management:** Create, view, update, and delete student records through a web-based interface.
- **Search Functionality:** Search student records by name, email, or place using Django ORM queries.
- **Sorting:** Sort student records by name, age, and date of birth.
- **Pagination:** Display five student records per page for easier navigation.
- **Dashboard Statistics:** Display total students, matching search results, and currently displayed records.
- **Delete Confirmation:** Confirm before permanently deleting a student record.
- **Responsive Interface:** Bootstrap-based dashboard with reusable Django templates.
- **Automated Testing:** Django unit tests covering models, CRUD operations, search, sorting, and pagination.

## Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Django 5.2.7 |
| Frontend | HTML5, CSS3, Bootstrap, JavaScript |
| Database | SQLite |
| Database Operations | Django ORM |
| Testing | Django TestCase |
| Version Control | Git, GitHub |
| Deployment | PythonAnywhere, WSGI |

## Project Architecture

StudentHub follows Django's Model-View-Template (MVT) architecture.

- **Model:** Defines student data and manages database interactions through Django ORM.
- **View:** Processes HTTP requests and handles CRUD operations, search, sorting, and pagination.
- **Template:** Renders the user interface using HTML, Bootstrap, CSS, and Django template tags.
- **Database:** SQLite stores student records.

## Project Structure

```text
studenthub-django-fullstack/
├── fvbcrudproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── myapp/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── tests.py
├── templates/
│   └── myapp/
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Geethadr16/studenthub-django-fullstack.git
cd studenthub-django-fullstack
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root and configure the Django secret key.

```env
DJANGO_SECRET_KEY=replace-with-your-own-secure-secret-key
```

Do not commit the `.env` file or real secret keys to GitHub.

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open the application at:

http://127.0.0.1:8000/

## Automated Testing

StudentHub includes **11 automated tests** using Django's built-in testing framework.

The test suite covers:

- Student model functionality
- Student creation and retrieval
- Student record updates and deletion
- Search functionality
- Sorting functionality
- Pagination behavior

Run the tests using:

```bash
python manage.py test myapp
```

## Deployment

StudentHub is deployed on **PythonAnywhere** using a Python virtual environment and Django's WSGI interface.

Deployment activities included:

1. Cloning the GitHub repository to PythonAnywhere.
2. Creating and activating a Python virtual environment.
3. Installing dependencies using `requirements.txt`.
4. Configuring environment variables for Django.
5. Applying database migrations.
6. Collecting static files using Django's `collectstatic` command.
7. Configuring WSGI, virtual environment, and static-file paths.
8. Configuring `ALLOWED_HOSTS` for the deployment domain.
9. Reloading the web application and verifying student record creation and retrieval.

**Live Website:** https://geethadr.pythonanywhere.com/

## Screenshots

Application screenshots will be added to demonstrate the student dashboard, registration form, search, and record-management interface.

## Key Learnings

- Developed a database-driven web application using Django's MVT architecture.
- Implemented CRUD operations using Django ORM.
- Built search, sorting, and pagination functionality for student records.
- Designed a responsive interface using Bootstrap and Django templates.
- Practiced automated testing using Django TestCase.
- Managed application source code using Git and GitHub.
- Gained practical experience deploying a Django application on PythonAnywhere.
- Configured environment variables, database migrations, WSGI, and static files for deployment.

## Future Improvements

- User authentication and role-based access control
- Enhanced form validation
- CI/CD automation using GitHub Actions

## Author

**Geetha D R**

GitHub: https://github.com/Geethadr16

**Project Repository:** https://github.com/Geethadr16/studenthub-django-fullstack
