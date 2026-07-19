from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange, ValidationError
from models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message='Username is required'),
        Length(min=3, max=80, message='Username must be 3-80 characters')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Email is required'),
        Email(message='Please enter a valid email address')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required'),
        Length(min=6, message='Password must be at least 6 characters')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(message='Please confirm your password'),
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Create Account')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already taken.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already registered.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email is required'),
        Email(message='Please enter a valid email address')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required')
    ])
    submit = SubmitField('Sign In')


class ReviewForm(FlaskForm):
    rating = IntegerField('Rating', validators=[
        DataRequired(message='Please select a rating'),
        NumberRange(min=1, max=5, message='Rating must be between 1 and 5')
    ])
    review_text = TextAreaField('Your Review', validators=[
        DataRequired(message='Please write your review'),
        Length(min=10, max=2000, message='Review must be 10-2000 characters')
    ])
    submit = SubmitField('Submit Review')


class BookForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(message='Title is required'),
        Length(max=200, message='Title cannot exceed 200 characters')
    ])
    author = StringField('Author', validators=[
        DataRequired(message='Author is required'),
        Length(max=150, message='Author cannot exceed 150 characters')
    ])
    genre = StringField('Genre', validators=[
        DataRequired(message='Genre is required'),
        Length(max=100, message='Genre cannot exceed 100 characters')
    ])
    description = TextAreaField('Description', validators=[
        DataRequired(message='Description is required'),
        Length(min=20, message='Description must be at least 20 characters')
    ])
    cover_image = StringField('Cover Image URL (Optional)', validators=[
        Length(max=300, message='URL cannot exceed 300 characters')
    ])
    submit = SubmitField('Add Book')