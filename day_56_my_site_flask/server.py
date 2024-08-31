from flask import Flask, render_template
import datetime


app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.date.today().year
    return render_template("index.html", current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
