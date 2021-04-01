import mysql.connector

#TODO
hostname = 'localhost'
username = 'username'
password = 'password'
database = 'dbname'

myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )

cursor = myConnection.cursor()

insert_stmt = (
  "INSERT INTO users (nome, idade, altura, peso) "
  "VALUES (%s, %s, %s, %s)"
)