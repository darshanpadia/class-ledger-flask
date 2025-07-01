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

<pre lang="nohighlight"><code>## 🗂️ Project Structure <code>class-ledger-flask/ ├── app.py # App factory ├── wsgi.py # Entry point ├── .env-sample # Sample environment variables ├── requirements.txt # Dependencies │ ├── models/ # SQLAlchemy models │ ├── __init__.py │ ├── teacher.py │ ├── student_record.py │ └── edit_log.py │ ├── routes/ # Blueprint-based routes │ ├── __init__.py │ ├── auth_routes.py │ └── dashboard_routes.py │ ├── services/ # Business logic layer │ ├── auth_services.py │ ├── dashboard_services.py │ └── teacher_services.py │ ├── repositories/ # DB access layer │ ├── teacher_repo.py │ ├── student_record_repo.py │ └── edit_log_repo.py │ ├── templates/ # Jinja2 templates │ ├── auth_templates/ │ └── dashboard_templates/ │ ├── forms/ # Flask-WTF forms │ ├── __init__.py │ ├── auth_forms.py │ ├── dashboard_forms.py │ └── common_forms.py │ ├── extensions.py # Flask extensions (DB, CSRF, Migrate) └── config.py # App configuration </code></pre>


---

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
Python 3.x

Flask

Flask-WTF

SQLAlchemy

Flask-Migrate

Bootstrap (frontend)


🧩 Scalability & Maintainability

✅ Separation of concerns via:

Routes – for request handling

Services – for business logic

Repositories – for DB interactions

✅ CSRF-safe forms and secure session-based login

✅ Easily extendable to support roles, pagination, analytics, and more

✅ Clear naming conventions and layered design for collaboration

