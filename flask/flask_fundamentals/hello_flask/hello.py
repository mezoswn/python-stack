from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'
if __name__=="__main__":    
    app.run(debug=True) 
    
      # Return the string 'Hello World!' as a response
                                 # Ensure this file is being run directly and not from a different module
# @app.route('/success')    # import statements, maybe some other routes
# def success():
#     return "success"    # app.run(debug=True) should be the very last statement!
# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(f"hello {name}")
#     return "Hello, " + {name}
# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id
# if __name__=="__main__":    
#     app.run(debug=True)    # Run the app in debug mode.

