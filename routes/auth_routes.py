from flask import Blueprint, render_template, session, flash, redirect, url_for
from services.auth_services import authenticate_teacher
from forms import LoginForm

auth_routes = Blueprint('auth_routes', __name__)

# -------------------------------------
# Route: /login
# Handles both GET (render login page) and POST (form submission)
# -------------------------------------
@auth_routes.route('/login', methods=['POST', 'GET'])
def teacher_login():
    form = LoginForm()

    # If form was submitted and passed all validators
    if form.validate_on_submit():
        username = form.teacher_username.data
        password = form.teacher_password.data

        teacher = authenticate_teacher(username, password)

        if teacher:
            # Store teacher ID in session to track login
            session['teacher_id'] = teacher.id
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password.", "error")  

    # For GET requests or failed POST, show the login page again
    return render_template('auth_templates/login.html', form=form)

