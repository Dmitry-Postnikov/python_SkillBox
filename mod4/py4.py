import subprocess

from flask import Flask

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    UPTIME = str(subprocess.check_output(["wsl", 'uptime']))
    print(UPTIME)
    UPTIME = UPTIME[UPTIME.find("up") + 2:UPTIME.find("users") - 5]
    return f"Current uptime is {UPTIME}"


if __name__ == '__main__':
    app.run(debug=True)