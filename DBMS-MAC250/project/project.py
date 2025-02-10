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
# query = """CREATE TABLE ins(
#             ins_code CHAR(5) PRIMARY KEY,
#             ins_name CHAR(30),
#             address CHAR(30),
#             city CHAR(30),
#             state CHAR(2),
#             zipcode CHAR(5));"""

# query = """CREATE TABLE patients(
#             p_code CHAR(5) PRIMARY KEY,
#             p_name CHAR(30),
#             ins_code CHAR(5),
#             address_line1 CHAR(30),
#             address_line2 CHAR(30),
#             city CHAR(30),
#             state CHAR(2),
#             zipcode CHAR(5),
#             FOREIGN KEY(ins_code) REFERENCES ins(ins_code));"""

# query = """CREATE TABLE mds(
#             mds_code CHAR(5) PRIMARY KEY,
#             mds_name CHAR(30),
#             address CHAR(30),
#             city CHAR(30),
#             state CHAR(2),
#             zipcode CHAR(5));"""

query = """CREATE TABLE medical(
            mp_code CHAR(5) PRIMARY KEY,
            description CHAR(30),
            price DECIMAL(6,2));"""
cursor.execute(query)
