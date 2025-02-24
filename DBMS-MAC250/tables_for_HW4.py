import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'library'
)

def query_mysql_executor(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        for row in result:
            print(row)
        print('-----------------------------------------------')
    except Exception as e:
        print(f"query failed: {e}")

database = """CREATE DATABASE library;"""
query_mysql_executor(query=database, conn=conn)

table1 = """CREATE TABLE patron(
            pat_id CHAR(4) PRIMARY KEY,
            pat_FName CHAR(15),
            pat_LName CHAR(15),
            pat_type CHAR(15));"""
query_mysql_executor(query=table1, conn=conn)

table2 = """CREATE TABLE book(
            bookNum CHAR(4) PRIMARY KEY,
            book_title CHAR(100).
            book_year CHAR(4),
            book_cost DECIMAL(6,2),
            book_subject CHAR(15),
            pat_id CHAR(4),
            FOREIGN KEY(pat_id) REFERENCES patron(pat_id));"""
query_mysql_executor(query=table2, conn=conn)

table3 = """CREATE TABLE checkout(
            checkNum CHAR(5) PRIMARY KEY,
            bookNum CHAR(4),
            pat_id CHAR(4),
            check_out_date DATE,
            check_due_date DATE,
            check_in_date DATE,
            FOREIGN KEY(bookNum) REFERENCES book(bookNum),
            FOREIGN KEY(pat_id) REFERENCES patron(pat_id));"""
query_mysql_executor(query=table3, conn=conn)

table4 = """CREATE TABLE author(
            au_id CHAR(3) PRIMARY KEY,
            au_FName CHAR(15),
            au_LName CHAR(15),
            au_birthYear CHAR(4));"""
query_mysql_executor(query=table4, conn=conn)

table5 = """CREATE TABLE writes(
            bookNum CHAR(4),
            au_id CHAR(3),
            PRIMARY KEY(bookNum, au_id),
            FOREIGN KEY(bookNum) REFERENCES book(bookNum),
            FOREIGN KEY(au_id) REFERENCES author(au_id));"""
query_mysql_executor(query=table5, conn=conn)


if conn:
    conn.close()
