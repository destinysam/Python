from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField,FileAllowed
from wtforms.fields import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from Main.models import User
