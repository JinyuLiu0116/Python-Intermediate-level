import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649'
)

cursor = conn.cursor()

query ="""CREATE DATABASE doctor;"""
cursor.execute(query)
