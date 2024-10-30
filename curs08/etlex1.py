# """Analiza comenzilor dintr-un magazin online"""

import pandas
import mysql.connector
from password import parola



# 1. EXTRAGEREA = conectarea la baza de date existenta adsgrupa2 si preluarea datelor:
my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=parola,
    database='adsgrupa2'
)
cursor = my_db.cursor()
# preiau date din doua tabele: products si orders
# cursor.execute('CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'name VARCHAR(100),'
#                'category VARCHAR(100),'
#                'price DECIMAL(10, 2))')
# cursor.execute('CREATE TABLE orders (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'product_id INT,' #este un FK catre products
#                'quantity INT,'
#                'order_date DATE,'
#                'FOREIGN KEY (product_id) REFERENCES products(id))')
# sql_products = 'INSERT INTO products (name, category, price) VALUES (%s, %s, %s)'
# val_products = [
#     ('Laptop', 'Electrocasnice', 1500.00),
#     ('Telefon', 'Electrocasnice', 800.00)
# ]
# cursor.executemany(sql_products, val_products)
# sql = 'INSERT INTO orders (product_id, quantity, order_date) VALUES (%s, %s, %s)'
# val = [
#     (1, 2, '2023-09-01'),
#     (2, 1, '2023-09-02')
# ]
# cursor.executemany(sql, val)
# my_db.commit()
# FINAL PARTE DE EXTRAGERE


# 2. TRANSFORMAREA DATELOR
# aici facem o analiza raport vanzari in functie de total

query = ('SELECT o.id, p.name, p.category, o.quantity, p.price'
         ' from orders o JOIN products p ON o.product_id = p.id') # vreau 2 informatii din 2 tabele
df = pandas.read_sql(query, my_db)
print(df)

# adaug inca o coloana numita total:
df['total'] = df['quantity'] * df['price']
print(df)

# LOAD = INCARCAREA DATELOR NOI

# a. INTR-UN CSV
df.to_csv('raport_vanzari.csv', index=False)
# b. IN BAZA DE DATE INTR-UN TABEL
# cursor.execute('CREATE TABLE raport_vanzari (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'name VARCHAR(100),'
#                'category VARCHAR(100),'
#                'quantity INT,'
#                'price DECIMAL(10,2),'
#                'total DECIMAL(10, 2))')
sql = 'INSERT INTO raport_vanzari (name, category, quantity, price, total) VALUES (%s, %s, %s, %s, %s)'
lista = []
for item, row in df.iterrows():
    lista.append(row.tolist()[1:]) # [1:] pt ca avem un header
cursor.executemany(sql, lista)
my_db.commit()



