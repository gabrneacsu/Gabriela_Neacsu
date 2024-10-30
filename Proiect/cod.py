import pandas
import mysql.connector
from password import parola
import matplotlib.pyplot as plot

# 1.
# a.
# conectarea la baza de date existenta adsgrupa2 si preluarea datelor:
my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=parola,
    database='baza_de_date'
)
cursor = my_db.cursor()
# cursor.execute('CREATE DATABASE baza_de_date') #aici creez baza de date

# citim datele din tabelul de orders:
query_orders = 'SELECT * FROM orders' #iau tot tot din orders
df_orders = pandas.read_sql(query_orders, my_db)
# print(df_orders)

# citim datele din tabelul de customers:
query_customers = 'SELECT * FROM customers' #iau tot tot din customers
df_customers = pandas.read_sql(query_customers, my_db)
# print(df_customers)

# citim datele din tabelul de products:
query_products = 'SELECT * FROM products' #iau tot tot din products
df_products = pandas.read_sql(query_products, my_db)
# print(df_products)

# citim datele din tabelul de reviews:
query_reviews = 'SELECT * FROM reviews' #iau tot tot din reviews
df_reviews = pandas.read_sql(query_reviews, my_db)
# print(df_reviews)



# # b
# # verificam valorile lipsa din orders
# valori_lipsa_orders = df_orders.isnull().sum()
# print(valori_lipsa_orders) # imi afiseaza cate valori sunt lipsa; daca sunt 0, inseamna ca datele noastre sunt complete
# # daca am valori lipsa fac asa:
# df_cu_valori_sterse_orders = df_orders.dropna() #aici ar fi sters randurile care au valori lipsa
#
# # verificam valorile lipsa din customers
# valori_lipsa_customers = df_customers.isnull().sum()
# print(valori_lipsa_customers) # imi afiseaza cate valori sunt lipsa; daca sunt 0, inseamna ca datele noastre sunt complete
# # daca am valori lipsa fac asa:
# df_cu_valori_sterse_customers = df_orders.dropna() #aici ar fi sters randurile care au valori lipsa
#
# # verificam valorile lipsa din products
# valori_lipsa_products = df_products.isnull().sum()
# print(valori_lipsa_products) # imi afiseaza cate valori sunt lipsa; daca sunt 0, inseamna ca datele noastre sunt complete
# # daca am valori lipsa fac asa:
# df_cu_valori_sterse_products = df_products.dropna() #aici ar fi sters randurile care au valori lipsa
#
# # verificam valorile lipsa din reviews
# valori_lipsa_reviews = df_reviews.isnull().sum()
# print(valori_lipsa_reviews) # imi afiseaza cate valori sunt lipsa; daca sunt 0, inseamna ca datele noastre sunt complete
# # daca am valori lipsa fac asa:
# df_cu_valori_sterse_reviews = df_reviews.dropna() #aici ar fi sters randurile care au valori lipsa

# 2.
# a.
# df_orders['order_date'] = pandas.to_datetime(df_orders['order_date'], errors='coerce')
#
# df_orders = df_orders.dropna(subset=['order_date'])
#
# df_orders['revenue'] = df_orders['quantity'] * df_orders['price']
#
# df_orders['year_month'] = df_orders['order_date'].dt.to_period('M')
#
# monthly_revenue = df_orders.groupby('year_month')['revenue'].sum().reset_index()
#
# print(monthly_revenue)
# # b.
# # query = ('SELECT p.product_name, p.category, o.quantity'
# #          ' from orders o JOIN products p ON o.product_id = p.product_id') # vreau informatii din 2 tabele
#
#
# query_b = '''
#     SELECT p.product_name, p.category, o.quantity
#     FROM orders o
#     JOIN products p ON o.product_id = p.product_id
# '''
#
# df_produse = pandas.read_sql(query_b, my_db)
#
# # Grupam și ordonam
# df_produse_grupate = df_produse.groupby(['category', 'product_name'])['quantity'].sum().reset_index()
# df_produse_ordonate = df_produse_grupate.sort_values(['category', 'quantity'], ascending=[True, False])
# print("Cele mai vândute produse per categorie:\n", df_produse_ordonate)

#
# # c.
# query_c = '''
#     SELECT c.name, o.price, o.quantity
#     FROM orders o
#     JOIN customers c ON o.customer_id = c.customer_id
# '''
#
# df_comenzi_clienti = pandas.read_sql(query_c, my_db)
# # coloana care contine venitul per comanda
# df_comenzi_clienti['revenue'] = df_comenzi_clienti['quantity'] * df_comenzi_clienti['price']
# # gruparea datelor in functie de numele clientului pt a obtine valoarea totala a comenzilor pt fiecare client
# df_comenzi_clienti_grupate = df_comenzi_clienti.groupby('name')['revenue'].sum().reset_index()
# df_comenzi_clienti_grupate = df_comenzi_clienti_grupate.rename(columns={'revenue': 'total_revenue'})
# # sortare in ordine descrescatoare
# df_comenzi_clienti_ordonat = df_comenzi_clienti_grupate.sort_values(by='total_revenue', ascending=False)
# print(df_comenzi_clienti_ordonat)

# # d.
# # Extragem datele din tabelele review și customers pentru a obține ID-ul clientului, ratingul și ID-ul produsului
# query_customers_review = '''
#     SELECT c.customer_id, r.rating, r.product_id
#     FROM reviews r
#     JOIN customers c ON r.customer_id = c.customer_id
# '''
#
# df_customers_review = pandas.read_sql(query_customers_review, my_db)
#
# # Extragem datele din tabelul products pentru a obține ID-ul produsului și numele acestuia
# query_products = '''
#     SELECT product_id, product_name
#     FROM products
# '''
#
# df_products = pandas.read_sql(query_products, my_db)
#
#
# # Facem join între DataFrame-urile obținute (df_customers_review și df_products) pe baza coloanei 'product_id'
# df_recenzii_produse = df_customers_review.merge(df_products, on='product_id')
#
#
# # media ratingurilor pentru fiecare produs
# recenzii_medie = df_recenzii_produse.groupby('product_name')['rating'].mean()
# print(recenzii_medie)
#

# # e.
# query_orders = '''
#     SELECT customer_id, order_id
#     FROM orders
# '''
#
# df_orders_clienti = pandas.read_sql(query_orders, my_db)
#
# # grupez comenzile după customer_id și număr comenzile pentru fiecare client
# df_orders_clienti['numar_comenzi'] = df_orders_clienti.groupby('customer_id')['order_id'].count()
#
# # sortare în ordine descrescătoare pentru a obține top 5 clienți -> cu head(5)
# df_orders_clienti = df_orders_clienti.sort_values(by='numar_comenzi', ascending=False).head(5)
#
# # Asociem numele clientului
# # Extrag numele clienților din tabelul customers
# query_customers = '''
#     SELECT customer_id, name
#     FROM customers
# '''
#
# df_customers = pandas.read_sql(query_customers, my_db)
#
# # join între df_top_clienti și df_customers pentru a adăuga numele clienților
# df_orders_clienti = df_orders_clienti.merge(df_customers, on='customer_id')
# print(df_orders_clienti)

#
# # 3.
# # a.
# # Extragem datele brute despre comenzi și clienți
# query_orders = 'SELECT customer_id, quantity, price FROM orders'
# query_customers = 'SELECT customer_id, country FROM customers'
#
# df_orders = pandas.read_sql(query_orders, my_db)
# df_customers = pandas.read_sql(query_customers, my_db)
#
# # Calculăm veniturile pentru fiecare comandă
# df_orders['revenue'] = df_orders['quantity'] * df_orders['price']
#
# # Alăturăm comenzile cu țările pentru a avea veniturile per țară
# df_orders_customers = df_orders.merge(df_customers, on='customer_id')
#
# # Agregăm veniturile pe fiecare țară
# df_country_sales = df_orders_customers.groupby('country')['revenue'].sum().reset_index()
# print(df_country_sales)
#
# # Creăm histograma
# df_country_sales['revenue'].hist(bins=5, color='skyblue', edgecolor='black')
# plot.xlabel('Vânzări totale')
# plot.ylabel('Frecvența')
# plot.title('Distribuția vânzărilor per țară')
# plot.show()

# # b.
# # Extragem datele despre comenzi
# query_orders = 'SELECT order_date, quantity, price FROM orders'
# # df_orders = pandas.read_sql(query_orders, my_db)
#
# df_orders['order_date'] = pandas.to_datetime(df_orders['order_date'], errors='coerce')
# #
# df_orders = df_orders.dropna(subset=['order_date'])
# #
# df_orders['revenue'] = df_orders['quantity'] * df_orders['price']
# #
# df_orders['year_month'] = df_orders['order_date'].dt.to_period('M')
# #
# monthly_revenue = df_orders.groupby('year_month')['revenue'].sum().reset_index()
#
#
# # Creăm graficul de tip linie
# monthly_revenue.plot(x='year_month', y='revenue', marker='o', linestyle='--', color='b', label='Venituri lunare')
# plot.xlabel('Lună')
# plot.ylabel('Venituri')
# plot.title('Grafic linie - Tendințele de vânzări lunare')
# plot.legend()
# plot.grid()
# plot.show()

# # c.
# # Extragem datele despre recenzii și produse
# query_reviews = 'SELECT product_id, rating FROM reviews'
# query_products = 'SELECT product_id, category FROM products'
#
# df_reviews = pandas.read_sql(query_reviews, my_db)
# df_products = pandas.read_sql(query_products, my_db)
#
# # Alăturăm recenziile cu categoriile produselor
# df_reviews_products = df_reviews.merge(df_products, on='product_id')
#
# # Calculăm media ratingurilor pe categorie
# df_category_ratings = df_reviews_products.groupby('category')['rating'].mean().reset_index()
# print(df_category_ratings)
#
# # Creăm graficul de tip bară
# df_category_ratings.plot.bar(x='category', y='rating', color='purple', alpha=0.7, edgecolor='black')
# plot.xlabel('Categorie')
# plot.ylabel('Media ratingurilor')
# plot.title('Media ratingurilor per categorie de produse')
# plot.show()

# # d.
# # Extragem datele despre comenzi și produse
# query_orders = 'SELECT product_id, quantity FROM orders'
# query_products = 'SELECT product_id, stock FROM products'
#
# df_orders = pandas.read_sql(query_orders, my_db)
# df_products = pandas.read_sql(query_products, my_db)
#
# # Calculăm numărul total de vânzări per produs
# df_sales_per_product = df_orders.groupby('product_id')['quantity'].sum().reset_index()
# df_sales_stock = df_sales_per_product.merge(df_products, on='product_id')
#
# print(df_sales_stock)
#
# # Creăm graficul scatter pentru a analiza corelația
# plot.scatter(df_sales_stock['stock'], df_sales_stock['quantity'], color='orange', alpha=0.6)
# plot.xlabel('Stoc disponibil')
# plot.ylabel('Numărul total de vânzări')
# plot.title('Corelația între stoc și numărul de vânzări')
# plot.show()

# # 4.
# # a.
# # Extragem datele despre comenzi și clienți
# query_orders = 'SELECT customer_id, order_id FROM orders'
# query_customers = 'SELECT customer_id, name FROM customers'
#
# df_orders = pandas.read_sql(query_orders, my_db)
# df_customers = pandas.read_sql(query_customers, my_db)
#
# # Calculăm numărul de comenzi per client și selectăm top 10
# df_top10_clienti = df_orders.groupby('customer_id').size().reset_index(name='numar_comenzi')
# df_top10_clienti = df_top10_clienti.sort_values(by='numar_comenzi', ascending=False).head(10)
#
# # Facem join între top 10 clienți și datele din customers pentru a obține numele
# df_top10_clienti = df_top10_clienti.merge(df_customers, on='customer_id')
# print(df_top10_clienti[['name', 'numar_comenzi']])


# # b.
# # Extragem datele despre recenzii și produse
# query_reviews = 'SELECT product_id FROM reviews'
# query_products = 'SELECT product_id, product_name FROM products'
#
# df_reviews = pandas.read_sql(query_reviews, my_db)
# df_products = pandas.read_sql(query_products, my_db)
#
# # Calculăm numărul de recenzii per produs
# df_top_produse = df_reviews.groupby('product_id').size().reset_index(name='numar_recenzii')
# df_top_produse = df_top_produse.sort_values(by='numar_recenzii', ascending=False)
#
# # Facem join între top produse și products pentru a obține numele produselor
# df_top_produse = df_top_produse.merge(df_products, on='product_id')
# print(df_top_produse[['product_name', 'numar_recenzii']])

# # c.
# # Extragem datele din tabelele orders și products
# query_orders = 'SELECT product_id, quantity FROM orders'
# query_products = 'SELECT product_id, category FROM products'
#
# df_orders = pandas.read_sql(query_orders, my_db)
# df_products = pandas.read_sql(query_products, my_db)
#
# # Alăturăm comenzile și categoriile de produse
# df_comenzi_categorii = df_orders.merge(df_products, on='product_id')
#
# # Grupăm și calculăm vânzările pe fiecare categorie
# df_vanzari_categorii = df_comenzi_categorii.groupby('category')['quantity'].sum().reset_index()
# df_vanzari_categorii = df_vanzari_categorii.sort_values(by='quantity', ascending=False)
# print(df_vanzari_categorii)









