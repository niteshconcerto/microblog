from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField ,TextAreaField
from wtforms.validators import ValidationError , DataRequired ,EqualTo ,Email,Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired() ,Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Reapeat Password', validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Sign In')


	def validate_username(self , username):
		user =User.query.filter_by(username = username.data).first()
		if user is not None:
			raise ValidationError("Please Select Different Username")

	def validate_email(self , email):
		user =User.query.filter_by(email = email.data).first()
		if user is not None:
			raise ValidationError("Please Select Different Email Address")


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')