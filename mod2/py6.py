import os

from flask import Flask

app = Flask(__name__)
BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


@app.route("/head_file/<int:size>/<path: RELATIVE_PATH>")
def head_file(SIZE: int, RELATIVE_PATH: str):
    abs_path = os.path.join(BASE_DIRECTORY, RELATIVE_PATH)
    with open(abs_path, 'r') as file:
        result_text = file.read(SIZE)
        result_size = len(result_text)
    return f'<b>{abs_path}</b> {result_size}<br>{result_text}'


if __name__ == "__main__":
    app.run(debug=True)
