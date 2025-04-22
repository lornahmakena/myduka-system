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

        for product in products:
            print(product)

        # Fetching sales
def fetch_sales_from_db():
        cur.execute("SELECT * FROM sales;")

        sales = cur.fetchall()

        for sale in sales:
            print(sale)

#inserting data

def insert_products():
      cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('sneakers',50000,60000,20)")
      conn.commit()


def insert_sales():
      cur.execute(f"insert into sales(pid,quantity,created_at)values(23,45,'{time}')")
      conn.commit()

insert_products()
insert_sales()

fetch_products_from_db()
fetch_sales_from_db()

