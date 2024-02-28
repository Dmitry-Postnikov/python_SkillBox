import random
from datetime import datetime, timedelta

from flask import Flask

app = Flask(__name__)

"""Задание 1"""
@app.route('/hello_world')
def hello_world():
    return f'Привет, мир!'

"""Задание 2"""
@app.route('/cars')
def cars():
    return f'Chevrolet, Renault, Ford, Lada'

"""Задание 3"""
@app.route('/cats')
def cats():
    return random.choice(['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин'])

"""Задание 4"""
@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now().time()
    return f"Точное время: {current_time}"

"""Задание 5"""
@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = (datetime.now() + timedelta(hours=1)).time()
    return f"Точное время через час будет {current_time_after_hour}"

"""Задание 6"""
@app.route('/get_random_word')
def get_random_word():
    with open('war_and_peace.txt', encoding='utf-8') as book:
        word = book.read()
    return random.choice(word.translate({ord(i): None for i in '.,!&:;«»„“'}).split())

"""Задание 7"""
counter = 0
@app.route('/counter')
def main():
    global counter
    counter += 1
    return str(counter)
