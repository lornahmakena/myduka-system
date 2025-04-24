#import flask
from flask import Flask

#instantiate your application - initialization of flask
app = Flask(__name__)

@app.route('/')
def home():
    pass

#run your app
app.run(debug=True)
