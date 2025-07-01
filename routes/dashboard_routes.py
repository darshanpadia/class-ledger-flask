from flask import Blueprint, render_template, url_for, flash, session, redirect
from forms import ActionForm,CreateStudentRecordForm
from services.dashboard_services import add_student_record_service, fetch_all_student_records, delete_student_record_service

dashboard_routes = Blueprint('dashboard_routes', __name__)

@dashboard_routes.route('/home')
def home():
    if 'teacher_id' not in session:
        return redirect(url_for('auth_routes.teacher_login'))
    student_records = fetch_all_student_records()
    action_form = ActionForm()
    create_student_record_form = CreateStudentRecordForm()
    return render_template('dashboard_templates/home.html', action_form=action_form,
                            create_student_record_form=create_student_record_form,
                            student_records=student_records
                            )

@dashboard_routes.route('/add_student', methods=['POST'])
def add_student_record():
    form = CreateStudentRecordForm()

    if form.validate_on_submit():
        result = add_student_record_service(
            student_name=form.student_name.data.strip(),
            subject=form.subject.data.strip(),
            marks=form.marks.data,
            teacher_id=session.get('teacher_id')
        )

        flash(result["message"], result["category"])
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{getattr(form,field).label.text}: {error}", "error")
    return redirect(url_for('dashboard_routes.home'))

@dashboard_routes.route('/delete/<int:record_id>', methods=['POST'])
def delete_student_record(record_id):
    if 'teacher_id' not in session:
        return redirect(url_for('auth_routes.teacher_login'))
    
    result = delete_student_record_service(record_id)
    flash(result["message"], result["category"])
    return redirect(url_for('dashboard_routes.home'))