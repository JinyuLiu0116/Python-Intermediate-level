import mysql.connector

conn = mysql.connector.connect(
    host = 'localhsot',
    user = 'root',
    password = '8551649',
    database = 'library'
)

def query_mysql_execute(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f"query failed: {e}")
    
# 1. Write a query to display the different subjects on which FACT has books. Include each subject only once 
query1 = """SELECT book_subject FROM book GROUP BY book_subject;"""
query_mysql_execute(query=query1,conn=conn)

# 2. Write a query to display the checkout number, book number, and checkout date of all books checked out before April 5, 2015
query2 = """SELECT checkNum, bookNum, check_out_date FROM checkout WHERE check_out_date < '2015-04-05';"""
query_mysql_execute(query=query2,conn=conn)

# 3. Write a query to display the book number, title, and year of publication of all books published 
# after 2013 and on the “Programming” subject
query3 = """SELECT bookNum, book_title, book_year
            FROM book
            WHERE book_year > '2013'
            AND book_subject = 'Programming';"""
query_mysql_execute(query=query3,conn=conn)
