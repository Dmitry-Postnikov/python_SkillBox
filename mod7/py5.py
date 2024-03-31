utils.py
handler = logging.handlers.TimedRotatingFileHandler(filename="utils.log", when='h', interval=10, backupCount=1)
formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s")
handler.setFormatter(formatter)

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
