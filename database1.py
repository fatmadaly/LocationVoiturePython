import mysql.connector
import sys

# create voiture tables

# sql_create = """
# CREATE TABLE IF NOT EXISTS VOITEURES ( 
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     Marque VARCHAR(250), 
#     Modele VARCHAR(250), 
#     Num_imma INT, 
#     Kilometrage INT, 
#     Etat INT, 
#     Prix_location FLOAT); """
    
  
# create locataires table
sql_create = """
CREATE TABLE IF NOT EXISTS VOITEURES ( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    Marque VARCHAR(250), 
    Modele VARCHAR(250), 
    Num_imma INT, 
    Kilometrage INT, 
    Etat INT, 
    Prix_location FLOAT); """

#connexion au base de données
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "pythonapp",
)

cursor = db.cursor()
cursor.execute(sql_create)

db.commit()