import psycopg2
from datetime import datetime

        # Connect to the database
conn = psycopg2.connect(
            user="postgres",
            password="lornahamy",
            host="localhost",
            port="5432",
            database="myduka"
        )

        # Execute db operations
cur = conn.cursor()

time = datetime.now()

def fetch_products_from_db():
        # query
        cur.execute("SELECT * FROM products;")

        products = cur.fetchall()
        return products

        # Fetching sales
def fetch_sales_from_db():
        cur.execute("SELECT * FROM sales;")

        sales = cur.fetchall()
        return sales

#inserting data

def insert_products():
      cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('sneakers',50000,60000,20)")
      conn.commit()
      return "product inserted"

def insert_sales():
      cur.execute(f"insert into sales(pid,quantity,created_at)values(23,45,'{time}')")
      conn.commit()
      return "sale made"

insert_products()
insert_sales()

fetch_products_from_db()
fetch_sales_from_db()


def profit_per_product():
      cur.execute("SELECT products.name,SUM((products.selling_price - products.buying_price) * quantity) AS profit FROM products JOIN sales ON products.id = sales.pid GROUP BY (products.name);")
      profit_per_product = cur.fetchall()
      return profit_per_product
                   
def profit_per_day():
       cur.execute("SELECT sales.created_at,SUM((products.selling_price - products.buying_price) * quantity) AS profit FROM  products JOIN  sales ON products.id = sales.pid GROUP BY (sales.created_at);")
       profit_per_day = cur.fetchall()
       return profit_per_day

def sales_per_product():
      cur.execute("SELECT products.name,SUM(products.selling_price * sales.quantity) AS revenue FROM products JOIN sales ON products.id = sales.pid GROUP BY (products.name);")
      sales_per_product = cur.fetchall()
      return sales_per_product

def sales_per_day():
      cur.execute("SELECT sales.created_at,SUM(products.selling_price * sales.quantity) AS revenue FROM products JOIN sales ON products.id = sales.pid GROUP BY (sales.created_at);")
      sales_per_day = cur.fetchall()
      return sales_per_day

profit_per_product()
profit_per_day()
sales_per_product()
sales_per_day()

def check_user(email):
      query = "SELECT * FROM users WHERE email = %s"
      cur.execute(query,(email,))
      user = cur.fetchone()
      return user

def add_user(user_details):
      query = "INSERT INTO users (name, email,phone, password) VALUES (%s, %s, %s, %s)"
      cur.execute(query,user_details)
      conn.commit()




























#task review
def fetch_data(table):
      cur.execute(f"select * from {table};")
      data = cur.fetchall()
      return data

#products = fetch_data('products')
#sales = fetch_data('sales')
#print("Products from fetch data func:\n",products)
#print("Products from fetch data func:\n",sales)



#insert products - method 1 takes values as parameters
def insert_ps(values):
      #use placeholders
      insert = "insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)"
      cur.execute(insert,values)
      conn.commit()

product_values = ("watches",500,1000,200)
product_values = ("apple",120,150,200)
insert_ps(product_values)
products = fetch_data('products')
print("Fetching data after modified func:\n",products)

#insert products - method 2 still takes values a parameter without placeholders
#replace with (values) parameter in formatted string
def insert_product2(values):
      insert =f"insert into products(name,buying_price,selling_price,stock_quantity)values{values}"
      cur.execute(insert)
      conn.commit()

#product_values = ("shoes",1500,2000,1000)
#insert_product2(product_values)
#products = fetch_data('products')
#print("Fetching prods method2:\n",products)

#method 3 - insert into multiple table with varying no. of columns
#insert into <table_name>(columns)values();
def insert_data(table,columns,values):
      cur.execute(f"insert into {table}({columns}) values{values}")
      conn.commit()

#table = 'products'
#columns = "name,buying_price,selling_price,stock_quantity"
#values = ("phone",8000,12000,100)
#insert_data(table,columns,values)
#products = fetch_data('products')
#print("data from last method:\n",products)


