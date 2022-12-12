from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired

class formIndex(FlaskForm):
    numberofdatain = FloatField('Amount', validators=[DataRequired()])
    measure = SelectField(u'TempA', choices=[(1, 'Celsius'), (2, 'Fahrenheit'), (3, 'Kelvin')], validators=[DataRequired()])
    mconverted = SelectField(u'TempB', choices=[(1, 'Celsius'), (2, 'Fahrenheit'), (3, 'Kelvin')], validators=[DataRequired()])
