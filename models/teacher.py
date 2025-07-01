from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Teacher(db.Model):
    """Represents a teacher with secure password handling."""

    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        """Hashes and sets the password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if a given password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Teacher {self.username}>"

    def __str__(self):
        return f"Teacher name is {self.username}"