# import Flask class object from flasj library
from flask import Flask

# instanciate the flask object
app=Flask(__name__)

# app.route defines the URL of the page relative to localhost
@app.route('/')
def home():
    return "home goes here"

@app.route('/about/')
def about():
    return "about page goes here"

if __name__=="__main__":
    app.run(debug=True)
