from repositories.teacher_repo import fetch_teacher_by_username

def authenticate_teacher(username, password):
    """
    Authenticate a teacher by verifying the username and password.
    
    Returns the Teacher object if credentials match, else None.
    """
    teacher = fetch_teacher_by_username(username)
    if teacher and teacher.check_password(password):
        return teacher
    return None
