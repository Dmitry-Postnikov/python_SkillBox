from flask import Flask
from flask_wtf import FlaskForm
from hw2_validators import number_length, NumberLength
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), number_length(10, 10), NumberLength(10, 10)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()


'''
Данные:
В эндпоинт /registration добавьте все валидаторы, о которых говорилось в последнем видео:

email (текст, обязательно для заполнения, валидация формата);
phone (число, обязательно для заполнения, длина — десять символов, только положительные числа);
name (текст, обязательно для заполнения);
address (текст, обязательно для заполнения);
index (только числа, обязательно для заполнения);
comment (текст, необязательно для заполнения).
'''


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Успешная регистрация пользователя {email} с номером телефона +7{phone}"

    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
