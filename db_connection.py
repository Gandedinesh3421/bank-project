import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dinnu@14",  
    database="banking_system"
)

cursor = db.cursor()
print("Database connected successfully!")
