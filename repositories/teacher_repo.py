from models.teacher import Teacher
from extensions import db

def fetch_teacher_by_username(username):
    """Return teacher by username."""
    return Teacher.query.filter_by(username=username).first()

def fetch_teacher_by_id(teacher_id):
    """Return teacher by ID."""
    return Teacher.query.get(teacher_id)

def insert_teacher(username, password_hash):
    """Insert a new teacher."""
    teacher = Teacher(username=username, password_hash=password_hash)
    db.session.add(teacher)
    db.session.commit()
    return 


