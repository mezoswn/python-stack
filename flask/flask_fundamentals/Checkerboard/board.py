# Done with Mohammed Raddad
from flask import Flask , render_template
app = Flask(__name__)
@app.route('/')
def drow():
    return render_template("board.html",down = 8 , across = 8)
@app.route('/<int:num>')
def drow2(num):
    return render_template("board.html",down = int(num) , across = 8)
@app.route('/<num>/<num1>')
def drow3(num,num1):
    return render_template("board.html",down = int(num) , across = int(num1))
@app.route('/<num>/<num1>/<col1>/<col2>')
def drow4(num,num1,col1,col2):
    return render_template("board.html",down = int(num) , across = int(num1),col1 = col1 , col2 = col2)
if __name__=="__main__":
    app.run(debug=True) 