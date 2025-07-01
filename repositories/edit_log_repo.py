from models.edit_log import EditLog
from extensions import db

def create_edit_log(teacher_username, record_id):
    """
    Create a new log entry for a student record edit.
    
    Args:
        teacher_username (str): The username of the teacher who edited the record.
        record_id (int): The ID of the student record that was edited.
    """
    log = EditLog(teacher_username=teacher_username, record_id=record_id)
    db.session.add(log)
    db.session.commit()