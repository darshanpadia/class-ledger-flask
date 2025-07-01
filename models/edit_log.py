from extensions import db
from datetime import datetime

class EditLog(db.Model):
    """Model to log student record edits by teachers."""
    
    __tablename__ = "edit_logs"

    id = db.Column(db.Integer, primary_key=True)
    teacher_username = db.Column(db.String(100), nullable=False)
    record_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
