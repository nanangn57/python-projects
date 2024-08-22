from flask import Flask
import random

app = Flask(__name__)
correct_num = random.randint(0, 9)


@app.route("/home")
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWNudmp0b3M1aWd2aDZqd3pnY21raHY2bzBtdzVwYncyY3d1bX' \
           'drbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13RcbHeXlLNysE/giphy.gif" width="480"/>'


@app.route("/home/<int:input_num>")
def guess_number(input_num):
    if input_num < correct_num:
        return '<h1 style="color:red; font-weight:bold">Too low, try again<h1/>' \
               '<iframe src="https://giphy.com/embed/vdief8MYYQmQiiYsMF" width="480" height="480" </iframe>'
    elif input_num > correct_num:
        return '<h1 style="color:purple; font-weight:bold">Too high, try again<h1/>' \
               '<iframe src="https://giphy.com/embed/3o6ZtaO9BZHcOjmErm" width="480" height="461" </iframe>'
    else:
        return '<h1 style="color:blue; font-weight:bold">You are correct<h1/>' \
               '<iframe src="https://giphy.com/embed/cXblnKXr2BQOaYnTni" width="480" height="398"</iframe>'


if __name__ == "__main__":
    app.run(debug=True)