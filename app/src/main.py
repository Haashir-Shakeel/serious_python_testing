from contextlib import redirect_stdout
from io import StringIO

from flask import Flask, request

port = 5000

print("Trying to run a socket server on:", port)


class PythonRunner:
    __globals = {}
    __locals = {}

    def run(self, code):
        f = StringIO()
        with redirect_stdout(f):
            exec(code, self.__globals, self.__locals)
        return f.getvalue()


pr = PythonRunner()


app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Enter Python code and tap "Run".'


@app.route("/python", methods=["POST"])
def run_python():
    try:
        return pr.run(request.json["command"])
    except Exception as e:
        return str(e)

@app.route("/alive", methods=["GET"])
def heartBeat():
    return "SERVER IS ONLINE"
    # return (jsonObject['name'])

app.run(port=port)