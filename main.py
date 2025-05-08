from flask import Flask,render_template,request,redirect,url_for
from database import fetch_products_from_db
from database import fetch_sales_from_db
from database import insert_ps
from database import insert_sales
from database import profit_per_product
from database import profit_per_day
from database import sales_per_product
from database import sales_per_day

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

@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
        product_id = request.form['p-id']
        quantity = request.form['quant']
        new_sale = (product_id,quantity)
        insert_sales(new_sale)
        return redirect(url_for('sales'))

@app.route('/dashboard')
def dashboard():
    profit_product = profit_per_product()
    profit_day = profit_per_day()
    sales_product = sales_per_product()
    sales_day = sales_per_day()

    #list comprehension
    product_name = [i[0] for i in profit_product]
    p_profit = [float (i[1]) for i in profit_product]
    p_sales = [float (i[1]) for i in sales_product]

    date = [i[0] for i in profit_day]
    p_day = [i[1] for i in profit_day]
    s_day = [i[1] for i in sales_day]

    return render_template('dashboard.html'product_name=product_name,p_profit=p_profit,p_sales=p_sales,
                           date=date, p_day=p_day,s_day=s_day )

@app.route('/users')
def users():
     return users

#run your app
app.run(debug=True)



