from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/test")
def dev_test_function():
    return f"Это текстовая страничка. Ответ сгенерирован в {datetime.now()}"

if __name__ == "__main__":
    app.run(debug=True)
