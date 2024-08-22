from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_bold():
        return f'<b>{function()}<b/>'
    return wrapper_bold


def make_italic(function):
    def wrapper_bold():
        return f'<em>{function()}<em/>'
    return wrapper_bold


def make_underline(function):
    def wrapper_bold():
        return f'<u>{function()}<u/>'
    return wrapper_bold


@app.route("/")
@make_bold
@make_italic
@make_underline
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
