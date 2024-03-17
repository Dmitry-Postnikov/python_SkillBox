from typing import Optional
from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError

'''Первый способ'''
def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        data = field.data
        if len(str(data)) < min or len(str(data)) > max:
            raise ValidationError(message=message)

    return _number_length

'''Второй способ(с помощью класса)'''
class NumberLength:
    def __init__(self, min: int, max: int, message: Optional = None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        if field.data <= 0 or len(str(field.data)) < self.min or len(str(field.data)) > self.max:
            raise ValidationError(message=self.message)