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

# 4. Write a query to display the book number, title, year of publication, subject, and cost 
# for all books that are on the subjects of “Middleware” or “Cloud,” and that cost more than $70
query4 = """SELECT bookNum, book_title, book_year, book_subject, book_cost
            FROM book
            WHERE book_subject IN ('Middleware', 'Cloud')
            AND book_cost > 70;""" # WHERE (book_subject = 'Middleware' OR book_subject = 'Cloud')
query_mysql_execute(query=query4,conn=conn)

# 5. Write a query to display the book number, title, and year of publication for all books that 
# contain the word “Database” in the title, regardless of how it is capitalized
query5 = """SELECT bookNum, book_title, book_year
            FROM book
            WHERE book_title LIKE '%DataBase%';"""

query_mysql_execute(query=query5,conn=conn)

# 6. Write a query to display the author ID, first and last name of all authors whose year of birth is unknown
query6 = """SELECT au_id, au_FName, au_LName
            FROM author
            WHERE au_birthYear IS NULL;"""
query_mysql_execute(query=query6,conn=conn)

# 7. Write a query to display the patron ID, full name (first and last), and patron type for all patrons. Sort 
# the results by patron type, then by last name and first name. Ensure that all sorting is case insensitive
query7 = """SELECT pat_idm, CONCAT(pat_FName, ' ', pat_LName) AS fullName, pat_type
            FROM patron
            ORDER BY pat_type, pat_LName, pat_FName;"""
query_mysql_execute(query=query7,conn=conn)

# 8. Write a query to display the book number and the number of times each book has been checked out. Do not 
# include books that have never been checked out.
query8 = """SELECT bookNum, COUNT(bookNum) AS 'Times Checked Out'
            FROM checkout
            WHERE check_out_date IS NOT NULL
            GROUP BY bookNum
            ORDER BY COUNT(bookNum) DESC;"""
query_mysql_execute(query=query8,conn=conn)
