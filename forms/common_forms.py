from flask_wtf import FlaskForm

class ActionForm(FlaskForm):
    """Empty form used to protect simple POST routes via CSRF token."""
    pass