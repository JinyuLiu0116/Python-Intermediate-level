import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'henry_books'
)

def query_mysql_executor(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(f"{row}")
    except Exception as e:
        print(f"query failed: {e}")

# 1. Create a view named Penguin Books. It consists of the book code, book title, book type, and book 
# price for every book published by Penguin USA. Display the data in the view.
query1 = """CREATE VIEW penguin_books AS SELECT b.book_code, b.title, b.type, b.price
            FROM book b, publisher p
            WHERE b.publisher_code = p.publisher_code
            AND p.publisher_name = 'Penguin USA';"""
query_mysql_executor(query=query1,conn=conn)

#  2. Create a view named Paperback. It consists of the book code, book title, publisher name, and 
# book price for every book that is available in paperback. Display the data in the view.
query2 = """CREATE VIEW paperback AS SELECT b.book_code, b.title, p.publisher_name, b.price
            FROM book b, publisher p
            WHERE b.publisher_code = p.publisher_code
            AND b.paperback = 'Y';"""
query_mysql_executor(query=query2,conn=conn)

#  3. Create a view named Book Inventory. It consists of the book code and the total number of units of 
# the book on hand at any branch. Display the data in the view.
query3 = """CREATE VIEW book_inventory AS SELECT b.book_code, SUM(i.on_hand) AS total_units
            FROM book b, inventory i
            WHERE b.book_code = i.book_code
            GROUP BY i.book_code;"""
query_mysql_executor(query=query3,conn=conn)

#  4. Create the following indexes. If it is necessary to name the index in your DB<S, use the indicated 
# name.
#  a. Create an index named BookIndex1 on the Publisher Name field in the Publisher 
# table.


#  b. Create an index named BookIndex2 on the Type field in the Book table.


#  c. Create an index named BookIndex3 on the Type and Price fields in the Book table 
# and list the prices in descending order.


#  5. Drop the BookIndex3 index.


#  6. Specify the integrity constraint that the price of any book must be less than $90.


#  7. Ensure that the following are foreign keys (that is, specify referential integrity) within the Henry 
# Books database,
#  a. PublisherCode is a foreign key in the Book table.


#  b. BranchNum is a foreign key in the Inventory table.


#  c. AuthorNum is a foreign key in the Wrote table.


#  8. Add to the Book table a new character field named Classic that is one character in length.


#  9. Change the Classic field in the Book table to Y for the book titled The Grapes of Wrath.


#  10. Change the length of the Title field in the Book table to 60.


#  11. What command would delete the Books table from the Henry Books database? (Do not delete the 
# book table).


#  12. Assume the Book table contains a column called TotalOnHand that represents the total units on 
# hand in all branches for that book. Following the style shown in the text, write the code for the 
# following triggers.
#  a. When inserting a row in the Inventory table, add the OnHand value to the TotalOnHand 
# value for the appropriate book.


#  b. When updating a row in the Inventory table, add the difference between the new OnHand 
# value and the OnHand value for the appropriate book.


#  c. When deleting a row in the Inventory table, subtract the OnHand value from the 
# TotalOnHand value for the appropriate book



if conn:
    conn.close()
