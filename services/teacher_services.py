from repositories.teacher_repo import fetch_teacher_by_username, insert_teacher
from werkzeug.security import generate_password_hash

def add_teacher_if_not_exists(username, password_hash):
    """
    Insert a new teacher only if the username doesn't already exist.
    """
    if not fetch_teacher_by_username(username):
        insert_teacher(username, password_hash)

def add_default_teachers():
    """
    Adds a predefined set of default teachers for testing/demo purposes.
    """
    password_hash = generate_password_hash("pass123")
    add_teacher_if_not_exists("teacher1",password_hash)
    add_teacher_if_not_exists("teacher2",password_hash)
