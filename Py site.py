from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Mnuygrcuyvyy!</p>"

@app.route("/<name>")
def hello_misha(name):
    return "<p>Hello, %s</p>" % name

if __name__ == "__main__":
    app.run()
