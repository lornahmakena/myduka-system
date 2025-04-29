from flask import Flask,render_template
from database import fetch_products_from_db
from database import fetch_sales_from_db


#instantiate your application - initialization of flask
app = Flask(__name__)

#routes
@app.route('/index')
def index():
    name = "Makena"
    numbers = [1,2,3,4,5]
    return render_template("index.html",data=name,numlist=numbers)

@app.route('/products')
def home():
    products = fetch_products_from_db()
    return render_template("products.html",products = products)

@app.route('/sales')
def about_us():
    sales = fetch_sales_from_db()
    return render_template("sales.html",sales = sales)

@app.route('/dashboard')
def dashboard():
    return "Dashboard"

@app.route('/contact_us')
def contact_us():
    return "Contact Us"

#run your app
app.run(debug=True)

