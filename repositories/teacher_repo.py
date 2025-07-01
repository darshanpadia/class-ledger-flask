from models.teacher import Teacher
from extensions import db

def fetch_teacher_by_username(username):
    """
    Fetch a Teacher object by username inside
    """
    return Teacher.query.filter_by(username=username).first()

def insert_teacher(username, password_hash):
    """
    Inser a new Teacher
    """
    teacher = Teacher(username=username, password_hash=password_hash)
    db.session.add(teacher)
    db.session.commit()
    return 

def fetch_teacher_by_id(teacher_id):
    return Teacher.query.get(teacher_id)
