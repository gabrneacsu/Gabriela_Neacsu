import pandas
import mysql.connector
from password import parola

# dataframe-ul din care voi prelua datele (Adica df):
df = pandas.read_csv('date_clienti.csv', header=None)
# header=none ca tabelul nostru nu are header, ci incepe direct cu datele
data_list = []
# conectarea la baza de date existenta adsgrupa2:
my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=parola,
    database='adsgrupa2'
)
# stabilesc conexiunea catre baza de date:
cursor = my_db.cursor()

# adaugarea tabelului in baza de date:
# cursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'name VARCHAR(100),'
#                'address VARCHAR(150),'
#                'city VARCHAR(100),'
#                'postal_code INT)')

# adaugarea unei coloane noi (utila daca ama creat tabela deja de ex si am uitat sa adaug vreo colana)
# cursor.execute('ALTER TABLE customers ADD COLUMN country VARCHAR(200)')

# REDENUMIREA UNEI COLOANE
# cursor.execute('ALTER TABLE customers RENAME COLUMN country TO country1')

# adaugarea datelor din dataframe in mysql:
# MOD 1:
# for item, row in df.iterrows():
#     customer_value = df.iloc[item, 0]
#     address_value = df.iloc[item, 1]
#     city_value = df.iloc[item, 2]
#     postal_code_value = df.iloc[item, 3]
#     country_value = df.iloc[item, 4]
#     data_list.append((customer_value, address_value, city_value, int(postal_code_value), country_value))
# print(data_list) # rezulta o lista mare de tupluri

# MOD 2:
# for item, row in df.iterrows():
#     data_list.append(row.tolist()) #valorile de pe rand sunt trecute intr-un tuplu
# print(data_list)

# trimiterea in baza de date sql:
sql = 'INSERT INTO customers (name, address, city, postal_code, country) VALUES (%s, %s, %s, %s, %s)'
cursor.executemany(sql, data_list) # .executemany-> ca sa execut toata lista de liste
my_db.commit()







"""
PROCESUL ETL (extract, transform, load)
Etape în procesul ETL:
1. Extract: Colectarea datelor din diverse surse (baze de date (mysql), fisiere (cvs, api etc)).
2. Transform: Curățarea, transformarea și manipularea datelor.
3. Load: Încărcarea datelor prelucrate într-o bază de date sau alt sistem.

"""