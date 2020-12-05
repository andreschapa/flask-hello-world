#import the Flask class from the flask package

from flask import Flask
#create the application object
app=Flask(__name__)

#error handling
app.config["DEBUG"]= True
#use the decorator pattern to link the view function to a URL
@app.route("/")
@app.route("/hello")

#define the view function which returns a string
def hello_world():
    return"YOOOOOOOOOOOOOOOOOOOOOO"

#start the development server using the run() method
@app.route("/test/<search_query>")
def search(search_query):
    return search_query


##test

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1) 
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"


@app.route("/name/<name>")
def index(name):
    if name.lower()=="michael":
        return f"Hello, {name}", 200
    else:
        return "Not Found",404


if __name__== "__main__":
    app.run()

