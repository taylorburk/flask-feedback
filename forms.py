from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm



class RegisterForm(FlaskForm): 
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)]) 
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8)]) 
    email = EmailField('Email', validators=[InputRequired(), Email()]) 
    first_name = StringField('First Name', validators=[InputRequired()]) 
    last_name = StringField('Last Name', validators=[InputRequired()])

class LoginForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )

class FeedbackForm(FlaskForm):

    title = StringField(
        "Title",
        validators=[InputRequired(), Length(max=100)],
    )
    content = StringField(
        "Content",
        validators=[InputRequired()],
    )


class DeleteForm(FlaskForm):
