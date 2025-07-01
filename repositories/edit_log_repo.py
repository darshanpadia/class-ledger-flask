from models.edit_log import EditLog
from extensions import db

def create_edit_log(teacher_username, record_id):
    log = EditLog(teacher_username=teacher_username, record_id=record_id)
    db.session.add(log)
    db.session.commit()