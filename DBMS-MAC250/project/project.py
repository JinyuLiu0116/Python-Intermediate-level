import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'doctor'
)

cursor = conn.cursor()

# query ="""CREATE DATABASE doctor;"""
# cursor.execute(query)
query = """CREATE TABLE ins(
            ins_code CHAR(5) PRIMARY KEY,
            ins_name CHAR(30),
            address CHAR(30),
            city CHAR(30),
            state CHAR(2),
            zipcode CHAR(5));"""
cursor.execute(query)
