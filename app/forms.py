from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired,Email

class ContactForm(FlaskForm):
    name    = StringField("Name", validators         = [DataRequired(message = "Input Required")])
    email   = StringField("Email Address",validators = [DataRequired(message = "Input Required"),Email(message = "Incorrect Format")])
    subject = StringField("Subject",validators       = [DataRequired(message = "Input Required")])
    message = TextAreaField("Message", validators    = [DataRequired(message = "Input Required")])
    