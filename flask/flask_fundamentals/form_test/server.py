from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index() :
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print("submitted info")
    name=request.form['name']
    location=request.form['location']
    language=request.form['language']
    comment=request.form['comment']
    return render_template("show.html",name=name,location=location,language=language,comment=comment)

if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, render_template, request, redirect # added request
# app = Flask(__name__)
# @app.route('/users')
# def user():
#     return render_template
# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     name_from_form = request.form['name']
#     email_from_form = request.form['email']
#     return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)
# if __name__ == "__main__":
#         app.run(debug=True)




# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/')
# def index() :
#     return render_template("index.html")
# if __name__ == "__main__":
#     app.run(debug=True)









