from flask import Flask
from flask import render_template
from flask import request
import utils
import random


HOST = "127.0.0.1"
PORT = 9999
TEXT = str(random.random()) + "http://{host}:{port}/".format(host=HOST, port=PORT)

app = Flask(__name__)


@app.route("/")
def hello():
    # return render_template("index.html", host=HOST)
    return render_template("bypass_referer.html", host=HOST)


@app.route("/saveticket/", methods=['GET'])
def send():
    msg = request.args.get("msg")
    sina = utils.save_ticket(msg)
    session = utils.get_session(sina)

    if session:
        utils.send_weibo(TEXT, session, sina['uid'])
    return 'aaa'


if __name__ == "__main__":
    app.run("0.0.0.0", PORT)
