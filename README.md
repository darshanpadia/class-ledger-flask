# Class Ledger Flask 🧾

A scalable and structured Flask web application for managing student records per teacher — with secure login, CSRF protection, edit tracking, and modular architecture.

---

## 🚀 Features

- 🧑‍🏫 Teacher login (secure hashed passwords)
- 📋 CRUD operations for student records (add/edit/delete)
- ✅ CSRF protection via Flask-WTF
- 🕵️ Duplicate handling & validation (e.g., merge on duplicate entry)
- 📝 Logging of all record edits (timestamp, teacher identity)
- 🧱 Modular architecture (routes, services, repositories)
- 💡 Scalable, testable project structure

---

## 🗂️ Project Structure

```
class-ledger-flask/
├── .env-sample
├── .gitignore
├── app.py
├── config.py
├── extensions.py
├── forms/
│   ├── __init__.py
│   ├── auth_forms.py
│   ├── common_forms.py
│   └── dashboard_forms.py
├── migrations/
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       ├── 36a7ddc71eb7_add_editlog.py
│       ├── 48a1a56d4f42_add_studentrecord.py
│       └── f8d7210376c3_setup_with_teacher.py
├── models/
│   ├── __init__.py
│   ├── edit_log.py
│   ├── student_record.py
│   └── teacher.py
├── README.md
├── repositories/
│   ├── edit_log_repo.py
│   ├── student_record_repo.py
│   └── teacher_repo.py
├── requirements.txt
├── routes/
│   ├── __init__.py
│   ├── auth_routes.py
│   └── dashboard_routes.py
├── services/
│   ├── auth_services.py
│   ├── dashboard_services.py
│   └── teacher_services.py
├── static/
│   ├── auth.css
│   └── dashboard.css
├── templates/
│   ├── auth_templates/
│   │   └── login.html
│   └── dashboard_templates/
│       └── home.html
└── wsgi.py
```


## 🚀 Project Setup Instructions (class-ledger-flask)

1. **Clone the Repository or Download ZIP**  
   - Option 1: Clone the repository  
     ```bash
     git clone <repo-url>
     cd class-ledger-flask
     ```
   - Option 2: Download the ZIP, extract it, and open the folder named `class-ledger-flask`.

2. **Create and Activate Virtual Environment**  
   - For **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\Activate.ps1  # If using PowerShell
     ```
   - For **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Required Dependencies**  
   ```bash
   pip install -r requirements.txt

4. **Configure Environment and Run the App**  
   - Rename `.env-sample` to `.env` in the root directory:  
     ```bash
     mv .env-sample .env  # macOS/Linux  
     ren .env-sample .env  # Windows CMD/PowerShell
     or manually
     ```

5. **Start the application**
     - **Windows**:
       ```bash
       python wsgi.py
       ```
     - **macOS/Linux**:
       ```bash
       python3 wsgi.py
       ```

6. **Access the App in Browser and Login**  
   - Open your browser and go to:  
     ```
     http://127.0.0.1:5000
     ```
   - Sample teacher login credentials:  
     - Username: `teacher1` or `teacher2`  
     - Password: `pass123`


Sample Teacher Credentials for testing
| Username | Password |
| -------- | -------- |
| teacher1 | pass123  |
| teacher2 | pass123  |


📦 Tech Stack
```
Python 3.x

Flask

Flask-WTF

SQLAlchemy

Flask-Migrate

Bootstrap (frontend)
```


🧩 Scalability & Maintainability
```

✅ Separation of concerns via:

Routes – for request handling

Services – for business logic

Repositories – for DB interactions

✅ CSRF-safe forms and secure session-based login

✅ Easily extendable to support roles, pagination, analytics, and more

✅ Clear naming conventions and layered design for collaboration
```

