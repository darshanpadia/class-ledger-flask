from models import StudentRecord
from sqlalchemy import func
from extensions import db

def fetch_all_student_records():
    """Return all student records."""
    return StudentRecord.query.all()

def find_duplicate_record(student_name, subject):
    """Check if a student record with the same name and subject exists (case-insensitive)."""
    return StudentRecord.query.filter(
        func.lower(StudentRecord.student_name) == student_name.lower(),
        func.lower(StudentRecord.subject) == subject.lower()
    ).first()

def insert_student_record(student_name, subject, marks, teacher_id):
    """Insert a new student record into the database."""
    new_record = StudentRecord(
        student_name=student_name,
        subject=subject,
        marks=marks,
        teacher_id=teacher_id
    )
    db.session.add(new_record)
    db.session.commit()

def update_student_record(record_id, name, subject, marks):
    """Update the student record with the given ID."""
    record = StudentRecord.query.get(record_id)
    if record:
        record.student_name = name
        record.subject = subject
        record.marks = marks
        db.session.commit()

def delete_student_record_by_id(record_id):
    """Delete a student record by ID."""
    record = StudentRecord.query.get(record_id)
    if record:
        db.session.delete(record)
        db.session.commit()
        return True
    return False

def fetch_student_by_id(record_id):
    """Fetch a single student record by its ID."""
    return StudentRecord.query.get(record_id)

