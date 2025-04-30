from flask import Flask,render_template,request,redirect,url_for
from database import fetch_products_from_db
from database import fetch_sales_from_db
from database import insert_ps


#instantiate your application - initialization of flask
app = Flask(__name__)

#routes
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/products')
def home():
    products = fetch_products_from_db()
    return render_template("products.html",products = products)

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['p-name']
        buying_price = request.form['b-price']
        selling_price = request.form['s-price']
        stock_quantity = request.form['quantity']

        new_product = (product_name,buying_price,selling_price,stock_quantity)
        insert_ps(new_product)

        return redirect(url_for('products'))
    

@app.route('/sales')
def about_us():
    sales = fetch_sales_from_db()
    return render_template("sales.html",sales = sales)

@app.route('/dashboard')
def dashboard():
    return "Dashboard"

#run your app
app.run(debug=True)


