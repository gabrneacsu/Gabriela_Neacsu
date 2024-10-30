"""Analiza vanzarilor intr-o companie"""

import pandas
import mysql.connector
from password import parola
# 1. partea de conectare
my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=parola,
    database='adsgrupa2'
)
cursor = my_db.cursor()


# cursor.execute('CREATE TABLE sales (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'region VARCHAR(50),'
#                'category VARCHAR(50),'
#                'sales_amount DECIMAL (10, 2),'
#                'sale_data DATE)')
# sql = 'INSERT INTO sales (region, category, sales_amount, sale_data) VALUES (%s, %s, %s, %s)'
# val = [
#     ('EST', 'Electrocasnice', 3000.00, '2024-01-01'),
#     ('VEST', 'Legume', 500.00, '2024-01-02'),
#     ('EST', 'Mobilier', 3000.00, '2024-02-01')
# ]
#
# cursor.executemany(sql, val)
# my_db.commit()

# 2.
# citim datele din tabelul de sales:
query = 'SELECT * FROM sales' #iau tot tot din sales de data asta
df_sales = pandas.read_sql(query, my_db)
print(df_sales)
# daca vreau gruparea pe regiuni
df_sales_grupat = df_sales.groupby('region')['sales_amount'].sum().reset_index()
print(df_sales_grupat)
# reset index are ca scop sa nu pastreze indexul anterior, ci o ia de la 0

# 3.
df_sales_grupat.to_csv('raport_vanzari_pe_regiuni.csv', index=False)
