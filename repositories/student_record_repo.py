from models import StudentRecord
from sqlalchemy import func
from extensions import db

def find_duplicate_record(student_name, subject):
    return StudentRecord.query.filter(
        func.lower(StudentRecord.student_name) == student_name.lower(),
        func.lower(StudentRecord.subject) == subject.lower()
    ).first()

def insert_student_record(student_name, subject, marks, teacher_id):
    new_record = StudentRecord(
        student_name=student_name,
        subject=subject,
        marks=marks,
        teacher_id=teacher_id
    )
    db.session.add(new_record)
    db.session.commit()

def update_student_record(record_id, name, subject, marks):
    record = StudentRecord.query.get(record_id)
    if record:
        record.student_name = name
        record.subject = subject
        record.marks = marks
        db.session.commit()