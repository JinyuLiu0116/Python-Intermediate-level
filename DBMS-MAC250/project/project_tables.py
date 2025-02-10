import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'doctor'
)

def query_mysql_executor(query, conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            print(cursor.fetchall())
    except Exception as e:
        print("Query is failed.")

#query ="""CREATE DATABASE doctor;"""

query1 = """CREATE TABLE ins(
            ins_code CHAR(5) PRIMARY KEY,
            ins_name CHAR(30),
            address CHAR(30),
            city CHAR(30),
            state CHAR(2),
            zipcode CHAR(5));"""
print(f"#1 {query_mysql_executor(query=query1,conn=conn)}")
query2 = """CREATE TABLE patients(
            p_code CHAR(5) PRIMARY KEY,
            p_name CHAR(30),
            ins_code CHAR(5),
            address_line1 CHAR(30),
            address_line2 CHAR(30),
            city CHAR(30),
            state CHAR(2),
            zipcode CHAR(5),
            FOREIGN KEY(ins_code) REFERENCES ins(ins_code));"""
print(f"#2 {query_mysql_executor(query=query2,conn=conn)}")
query3 = """CREATE TABLE mds(
            mds_code CHAR(5) PRIMARY KEY,
            mds_name CHAR(30),
            address CHAR(30),
            city CHAR(30),
            state CHAR(2),
            zipcode CHAR(5));"""
print(f"#3 {query_mysql_executor(query=query3,conn=conn)}")
query4 = """CREATE TABLE medical(
            mp_code CHAR(5) PRIMARY KEY,
            description CHAR(30),
            price DECIMAL(6,2));"""
print(f"#4 {query_mysql_executor(query=query4,conn=conn)}")
query5 = """CREATE TABLE treatments(
            p_code CHAR(5),
            mds_code CHAR(5),
            mp_code CHAR(5),
            date DATE,
            PRIMARY KEY(p_code, mds_code, mp_code));"""
print(f"#5 {query_mysql_executor(query=query5,conn=conn)}")

if conn:
    conn.close()
