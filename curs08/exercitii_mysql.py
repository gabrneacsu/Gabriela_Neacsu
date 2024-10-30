import mysql.connector
from matplotlib.backend_tools import Cursors

from password import parola

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=parola,
    database='adsgrupa2' #asa ma conectez la o baza de date deja existenta

)
cursor = my_db.cursor() #cursorul e ce ne ajuta pe noi sa executam respectiva comanda
# cursor.execute('CREATE DATABASE adsgrupa2') #aici creez baza de date

# doar o data cream tabela, dupa crapa, pt ca deja exista
# cursor.execute('CREATE TABLE projects (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'name VARCHAR(255),'
#                'address VARCHAR(255),'
#                'project_number INTEGER)')


# cursor.execute('CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'first_name VARCHAR(255),'
#                'last_name VARCHAR(255),'
#                'email VARCHAR(255))')

# cursor.execute('SHOW TABLES') # asa vad ce tabele am in baza de date
# for x in cursor:
#     print(x)

# cursor.execute('ALTER TABLE projects ADD COLUMN varsta INTEGER') # DACA AVEM DE MODIFICAT STRUCTURA A TABELEI (ADAUG COLOANA)
# cursor.execute('ALTER TABLE projects DROP COLUMN varsta') # DACA AVEM DE MODIFICAT STRUCTURA A TABELEI (STERG COLOANA)

# daca vreau sa inserez valori:
# sql = 'INSERT INTO projects (name, address, project_number) VALUES (%s, %s, %s)'
# val = [
#     ('Petre', 'Bucuresti', 123),
#     ('Amalia', 'Ploiesti', 321),
#     ('Mihai', 'Bacau', 224)
# ]
# cursor.executemany(sql, val)
# my_db.commit()

# daca vreau sa modif un anumit rand:
sql = 'UPDATE projects SET address="Bucuresti" where id=2'
cursor.execute(sql) #valideaza si face leg dintre sql si cursor
my_db.commit() #realizeaza executia la baza de date (necesar la insertii si update uri)






# denumirile coloanelor NU pot avea spatii intre cuvinte






"""
id-ul -> identificatorul unic al randului, ajuta la stabilirea relatiilor dintre tabele (primary key PK)
fiecare entitate are un id, cu ajutorul lui pot identifica pe ce id suntem cu legatura
foreign key - FK
"""
