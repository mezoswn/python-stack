### Done With Khalil AbuAyyash
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Please type play after slash"

@app.route('/play')
def level1():
    x = 3
    color = "blue"
    return render_template('index.html', x = 3, color = "blue")

@app.route('/play/<int:x>')
def level2(x):
    x = int(x)
    color = "blue"
    return render_template('index.html',x = x, color = "blue")

@app.route('/play/<int:x>/<color>')
def level3(x, color):
    x = int(x)
    return render_template('index.html',x = x, color = color)


if __name__ == "__main__":
    app.run(debug=True)