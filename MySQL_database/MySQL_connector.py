import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="8551649",
    database="stock_data"# after database has been created, we can add it to connector
)
# we can cursor through database and run the sql commend
mycursor = db.cursor()

mycursor.execute("CREATE DATABASE stock_data")