from flask import Flask,render_template

#instantiate your application - initialization of flask
app = Flask(__name__)

#routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/products')
def home():
    return render_template("products.html")

@app.route('/sales')
def about_us():
    return render_template("sales.html")

@app.route('/dashboard')
def dashboard():
    return "Dashbo"

@app.route('/contact_us')
def contact_us():
    return "Contact Us"

#run your app
app.run(debug=True)
