from werkzeug.routing import ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from config import Config

class LoginForm(FlaskForm):

   username = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])

   def validate_username(self, field):
       if field.data != Config.ADMIN_USERNAME:
           raise ValidationError("Invalid username")
       return field.data

   def validate_password(self, field):
       if field.data != Config.ADMIN_PASSWORD:
           raise ValidationError("Invalid password")
       return field.data