# 🎓 StudentHub — Student Management System

A full-stack **Student Management System** developed using Python, Django, SQLite, HTML, CSS, Bootstrap, and JavaScript.

StudentHub provides a responsive, database-driven dashboard for managing student records with CRUD operations, search, sorting, pagination, and dashboard statistics.

The application includes automated testing using Django's testing framework and is deployed on PythonAnywhere.

## 🌐 Live Demo

🚀 **Live Application:** https://geethadr.pythonanywhere.com/

💻 **GitHub Repository:** https://github.com/Geethadr16/studenthub-django-fullstack

☁️ **Deployment Platform:** PythonAnywhere

## ✨ Key Features

- 👨‍🎓 **Student Management:** Add, view, update, and delete student records.
- 🔍 **Search Functionality:** Search students by name, email, or place using Django ORM queries.
- ↕️ **Sorting:** Sort student records by name, age, and date of birth.
- 📄 **Pagination:** Display five student records per page.
- 📊 **Dashboard Statistics:** Display total students, matching records, and currently displayed records.
- 🗑️ **Delete Confirmation:** Confirm before permanently deleting student records.
- 📱 **Responsive Design:** Bootstrap-based interface with reusable Django templates.
- 🧪 **Automated Testing:** Django unit tests covering models, CRUD operations, search, sorting, and pagination.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| 🐍 Programming Language | Python |
| ⚙️ Backend | Django 5.2.7 |
| 🎨 Frontend | HTML5, CSS3, Bootstrap, JavaScript |
| 🗄️ Database | SQLite |
| 🔗 Database Operations | Django ORM |
| 🧪 Testing | Django TestCase |
| 🔧 Version Control | Git, GitHub |
| ☁️ Deployment | PythonAnywhere, WSGI |

## 🏗️ Project Architecture

StudentHub follows Django's **Model-View-Template (MVT)** architecture.

- 📦 **Model:** Defines student data and manages database interactions using Django ORM.
- ⚙️ **View:** Processes HTTP requests and handles CRUD operations, search, sorting, and pagination.
- 🎨 **Template:** Renders the user interface using HTML, Bootstrap, CSS, and Django template tags.
- 🗄️ **Database:** SQLite stores and retrieves student records.

## 📁 Project Structure

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

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Geethadr16/studenthub-django-fullstack.git
cd studenthub-django-fullstack
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY=replace-with-your-own-secure-secret-key
```

🔐 **Security:** Keep your `.env` file and actual secret keys out of GitHub.

### 6️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

### 7️⃣ Run the Development Server

```bash
python manage.py runserver
```

Open the application at http://127.0.0.1:8000/

## 🧪 Automated Testing

StudentHub includes **11 automated tests** implemented using Django's built-in testing framework.

### Test Coverage

- ✅ Student model functionality
- ✅ Student
