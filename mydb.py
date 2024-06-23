import psycopg2
from psycopg2 import sql

database= psycopg2.connect(
    host='localhost',
    user='postgres',
    password='root',
    
    
)
# Create a new connection to the default database without a transaction
database.set_session(autocommit=True)
#prepare cursor object
cursorObject=database.cursor()
#create a database
cursorObject.execute("CREATE DATABASE projectdb ")
database.commit()

print("All done") 