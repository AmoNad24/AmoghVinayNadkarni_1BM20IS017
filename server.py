from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, My Name is AmoghVinayNadkarni_1BM20IS017"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
