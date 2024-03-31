import logging.config
import logging_tree
from dict_configuration import dict_config
from flask import Flask
from mod7 import utils
from logging_tree import printout

app = Flask(__name__)

logging.config.dictConfig(dict_config)

logger = logging.getLogger("app")


@app.route("/addition/<float:a>/<float:b>")
def addition(a, b):
    logger.info("ÎŒØ∏‡°⁄·°€йцукен")
    logger.debug(f"Start endpoint /division, args: {a}, {b}")
    return str(utils.addition(a, b))


@app.route("/multiplication/<float:a>/<float:b>")
def multiplication(a, b):
    logger.info("ÎŒØ∏‡°⁄·°€йцукен")
    logger.debug(f"Start endpoint /division, args: {a}, {b}")
    return str(utils.multiplication(a, b))


@app.route("/subtraction/<float:a>/<float:b>")
def subtraction(a, b):
    logger.info("ÎŒØ∏‡°⁄·°€йцукен")
    logger.debug(f"Start endpoint /division, args: {a}, {b}")
    return str(utils.subtraction(a, b))


@app.route("/division/<float:a>/<float:b>")
def division(a, b):
    logger.info("ÎŒØ∏‡°⁄·°€йцукен")
    logger.debug(f"Start endpoint /division, args: {a}, {b}")
    return str(utils.division(a, b))


@app.route("/pow/<float:a>/<float:b>")
def pow(a, b):
    logger.info("ÎŒØ∏‡°⁄·°€йцукен")
    logger.debug(f"Start endpoint /division, args: {a}, {b}")
    return str(utils.pow(a, b))


if __name__ == "__main__":
    with open("logging_tree.txt", "w") as f:
        f.write(logging_tree.format.build_description())
    logger.info(f"Started")
    app.run(debug=True)
