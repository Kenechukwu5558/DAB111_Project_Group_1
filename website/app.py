from flask import Flask, render_template
import sqlite3
import pathlib

cwd = pathlib.Path.cwd()
basic_path = pathlib.Path(r'C:\Users\User1\OneDrive\Documents\KENE STUDY MATERIALS\DAB111.2\project\Kenechukwu5558\Database')
database_name = "customers.db"
database_path = basic_path / database_name
print(database_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(database_path)
    cursor = con.cursor()
    customer = cursor.execute("SELECT * FROM customer_data limit 20").fetchall()
    con.close()

    columns = ['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Total', 
               'Date', 'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income', 'Rating']
    

    return render_template("table_data.html", columns=columns, customer=customer)

if __name__=="__main__":
    app.run(debug=True)