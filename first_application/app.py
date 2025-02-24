from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/test")
def test_function():
    return f"Это текстовая страничка. Ответ сгенерирован в {datetime.now()}"

@app.route("/hello")
def hello_function():
    return f"Hello World. Ответ сгенерирован в {datetime.now()}"

counter = 0

@app.route("/counter")
def count():
    global counter
    counter += 1
    return f"Страница открыта {counter} раз(а)."

if __name__ == "__main__":
    app.run(debug=True)
