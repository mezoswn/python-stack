#done with Mohammed Raddad

from flask import Flask, app, session,render_template,redirect,request



app =Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def count():
    session['counter']=0
    return redirect("/count")

@app.route("/count")
def add_counter():
    count=session['counter']
    count=count+1
    session['counter']=count
    return render_template("counter.html",count=session['counter'])

@app.route("/destroy_session")
def clear():
   
    return redirect('/')

@app.route("/add_two")
def add():
    session['counter']+=2
    return render_template("counter.html",count=session['counter'])

@app.route("/sep",methods=["POST"])
def add1():
    
    
    request.form['number']
    session['counter']+= int(request.form['number'])
    session['theplus']=request.form['number']
    
    return redirect('/count')





if __name__=="__main__":
    app.run(debug=True)
