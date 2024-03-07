import datetime

from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])
    if check_date(year, month, day):
        storage.setdefault(year, {}).setdefault(month, 0)
        storage[year][month] += number
        return f'Данные зафиксированы. {storage}'
    else:
        return 'Введённые дата является некорректной. Запишите новую: '


def check_date(year, month, day):
    try:
        datetime.datetime(year, month, day)
        correct_date = True
    except ValueError:
        correct_date = False
    return correct_date


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    sum_expense = 0
    try:
        for expense in storage[year].values():
            sum_expense += expense
            return f'За {year} год расходы в общей сложности составляют {sum_expense} рублей.'
    except KeyError:
        return f'Данные по {year} году отсутствуютю'


@app.route("/calculate/<int: year>/<int:month>")
def calculate_month(year: int, month: int):
    try:
        return f'За {year} год {month} месяц расходы в общей сложности составляют {storage[year][month]}'
    except KeyError:
        return f'Данные по {year} году и {month} месяц отсутствуютю'


if __name__ == "__main__":
    app.run(debug=True)
