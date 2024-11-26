from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index_practice_form.html")


@app.route('/login', methods=["POST"])
def receive_data():
    if request.form['username'] and request.form['password']:
        return f"<h1> Name: {request.form['username']}, Password: {request.form['password']} </h1>"
    else:
        return 'Invalid username/password'
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)