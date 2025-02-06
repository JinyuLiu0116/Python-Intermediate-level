import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'premiere'
)

def query_mysql_executor(query, num, conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            print(f"#{num}: {result}\n")
    except Exception as e:
        raise Exception(f"Job Failed {e}")

    #List the part number, description, and price for part.
query = 'SELECT partNum, description, price FROM part'
num = 1
query_mysql_executor(query=query,num=num,conn=conn)


    #2.List all rows and columns for the complete orders table
query = 'SELECT * FROM orders;'
num = 2
query_mysql_executor(query=query,num=num,conn=conn)
    
#3.List the names of customers with credit limits of $10,000 or more.
query = 'SELECT customerName FROM customer WHERE creditLimit >= 10000;'
num = 3
query_mysql_executor(query=query,num=num,conn=conn)
    
#4.List the order number for each placed by customer number 608 on 10/23/2010
query = """SELECT orderNum FROM orders 
        WHERE customerNum = 608 AND orderDate = '2010-10-23';"""
num = 4
query_mysql_executor(query=query,num=num,conn=conn)
#5.List the number and name of each customer represented by sales rep 35 or sales rep 65
query = """
            SELECT customerNum, customerName FROM customer
            WHERE repNum = '35' OR repNum = '65';
        """
num = 5
query_mysql_executor(query=query,num=num,conn=conn)

#6.List the part number and part description of each part that is not in item class AP
query = """SELECT partNum, description FROM part WHERE class != 'AP';"""
num = 6
query_mysql_executor(query=query,num=num,conn=conn)
#7.List the part number, description, and number of units on hand for each part that
#  has between 10 and 25 units on hand, including both 10 and 25. Do this in two ways
query1 = """SELECT partNum, description, onHand FROM part WHERE onHand BETWEEN 10 AND 25;"""
query2 = """
            Select partNum, description, onHand FROM part
            WHERE onHand >= 10 AND onHand <= 25;
         """
num = 7.1
query_mysql_executor(query=query1,num=num,conn=conn)
num = 7.2
query_mysql_executor(query=query2,num=num,conn=conn)

#8.List the part number, part description, and on hand value of each part in item class SG
#  Assign the name ON_HAND_VALUE to the computed column.
query = """SELECT partNum, description, onHand * price AS ON_HAND_VALUE
           FROM part WHERE class = 'SG';"""
num = 8
query_mysql_executor(query=query,num=num,conn=conn)

#9.List the part number, part description, and onhand value for each part whose on hand
#  value is ate least$7,500. 
query = """SELECT partNum, description, onHand * price AS ON_HAND_VALUE
           FROM part WHERE onHand * price >= 7500;"""
num = 9
query_mysql_executor(query=query,num=num,conn=conn)
#10.Use the IN operator to list the part number and part description of each part in item class
#   AP or SG
query = """SELECT partNum, description FROM part
           WHERE class IN('AP', 'SG');"""
num = 10
query_mysql_executor(query=query,num=num,conn=conn)

#11.Find the number and name of each customer whose name begins with the letter"B"
query = """SELECT customerNum, customerName FROM customer
           WHERE customerName LIKE 'B%';"""
num = 11
query_mysql_executor(query=query,num=num,conn=conn)
#12.List all details about all parts. Order the output by part description
query = """SELECT * FROM part ORDER BY description;"""
num = 12
query_mysql_executor(query=query,num=num,conn=conn)
#13.List all details about all parts. order the output by part number
#   within warehouse(That is, order the output by warehouse and the by part number)
query = """SELECT * FROM part ORDER BY warehouse, partNum;"""
num = 13
query_mysql_executor(query=query,num=num,conn=conn)

#14.How many customers have balances that are more than their credit limits?
query = """SELECT COUNT(*) FROM customer
           WHERE balance > creditLimit;"""
num = 14
query_mysql_executor(query=query,num=num,conn=conn)
#15.Find the total of the balances for all customers represented by sales
#   rep 65 with balances that are less than their credit limits
query = """SELECT SUM(balance) FROM customer
           WHERE repNum = '65'
           AND balance < creditLimit;"""
num = 15
query_mysql_executor(query=query,num=num,conn=conn)

if conn:
    conn.close()
