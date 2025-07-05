from flask import Flask

'''
It creates an instance of the first class, which will be your WSGI (Web Server Gateway Interface) application.
'''

### WSGI application
app=Flask(__name__) 


@app.route("/")
def welcome():
  return "welcome to the this  course.This is an amazing course"


@app.route("/index")
def index():
  return "welcome to the this flask course.This is an amazing course"


if __name__ == "__main__":
  app.run(debug=True)