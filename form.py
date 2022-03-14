from flask_wtf import FlaskForm
import email_validator
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    email = StringField('Email', [Email(message='Incorrect email address'), DataRequired()])
    password = PasswordField('Password', [DataRequired(), Length(min=5, message="entered password is too short")])
    address1 = StringField('Address 1', [DataRequired()])
    address2 = StringField('Address 2', [DataRequired()])
    city = StringField('City', [DataRequired()])
    state = SelectField('State', choices=[('Vilnius', 'Vilnius'), ('Kaunas', 'Kaunas')], validators=[DataRequired()])
    zip_code = StringField('Zip Code', [DataRequired(), Length(min=4, message="entered zip code is too short")])
    check = BooleanField('I confirm that entered data is valid')
    submit = SubmitField("Submit")