from flask import Flask

app = Flask(__name__)


@app.route("/dd/")
def dd():
    return 'dd'


@app.route("/example/")
def example():
    return 'example'


@app.errorhandler(404)
def handle_exception(e: 404):
    lst = []
    for rule in app.url_map.iter_rules():
        url = "http://localhost:5000" + str(rule.rule)
        lst.append(f"<a href='{url}'>{url}</a>")
    return f"Запрошенный URL-адрес не был найден на сервере. Вы можете перейти по следующим ссылкам:<br>" \
           f"{'<br>'.join(lst[1:])}", 404


if __name__ == "__main__":
    app.run(debug=True)