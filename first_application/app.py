from flask import Flask
from datetime import datetime, timedelta
import random
import os
import re

app = Flask(__name__)

# Глобальные переменные
cars_list = ["Chevrolet", "Renault", "Ford", "Lada"]
cats_list = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
counter_visits = 0

# Определяем путь к файлу "Война и мир"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

# Загружаем слова из книги (делаем это один раз при запуске)
def load_words():
    if not os.path.exists(BOOK_FILE):
        return ["Файл", "не", "найден"]
    with open(BOOK_FILE, encoding='utf-8') as f:
        text = f.read()
    words = re.findall(r'\b\w+\b', text)  # Убираем знаки препинания
    return words

words_list = load_words()

@app.route("/hello_world")
def hello_world():
    return "Привет, мир!"

@app.route("/cars")
def cars():
    return ", ".join(cars_list)

@app.route("/cats")
def cats():
    return random.choice(cats_list)

@app.route("/get_time/now")
def get_time_now():
    current_time = datetime.now().strftime('%H:%M:%S')
    return f"Точное время: {current_time}"

@app.route("/get_time/future")
def get_time_future():
    future_time = (datetime.now() + timedelta(hours=1)).strftime('%H:%M:%S')
    return f"Точное время через час будет {future_time}"

@app.route("/get_random_word")
def get_random_word():
    return random.choice(words_list) if words_list else "Ошибка загрузки книги"

@app.route("/counter")
def counter():
    global counter_visits
    counter_visits += 1
    return f"Страница /counter открыта {counter_visits} раз(а)"

if __name__ == "__main__":
    app.run(debug=True)

