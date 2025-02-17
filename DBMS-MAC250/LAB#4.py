import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'premiere'
)

def query_mysql_executor(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f"query failed:{e}")

# 1 Create a view named major_customer. It consists of the customer number, name, balance, credit limit, 
# and rep number for every customer whose credit limit is $10000 or less.
# a.	Write and execute the CREATE VIEW command to create the major_customer view.
query1_a = """CREATE VIEW major_customer 
                AS SELECT customerNum, customerName, balance, creditLimit, repNum
                FROM customer
                WHERE creditLimit <= 10000;"""
query_mysql_executor(query= query1_a, conn=conn)

# b.Write and execute the command to retrieve the customer number and name of each customer 
# in the major_curstomer view with a balance that exceeds the credit limit.
query1_b = """SELECT customerNum, customerName FROM major_customer
                WHERE balance > creditLimit;"""
query_mysql_executor(query= query1_b, conn=conn)

#c.	Write and execute the query that the DBMS actually executes.
query1_c = """UPDATE major_customer 
                SET creditLimit = 10000
                WHERE customerNum = '148';"""
query_mysql_executor(query= query1_c, conn=conn)

# 2 Create a view named part_order. It consists of the par number, description, price, order number, 
# order date, number ordered, and quoted price for all order lines currently on file.
# a.	Write and execute the CREATE VIEW command to create the part_order view.
query2_a = """CREATE VIEW part_order
                AS SELECT p.partNum, p.description, p.price, o.orderNum, o.orderDate, ol.numOrdered, ol.quotedPrice
                FROM part p, orders o, orderline ol
                WHERE p.partNum = ol.partNum
                AND ol.orderNum = o.orderNum;"""
query_mysql_executor(query= query2_a, conn=conn)

# b.	Write and execute the command to retrieve the part number, description, order number, and quoted price for all orders 
# in the part_order view for parts with quoted prices that exceed $100.
query2_b = """SELECT partNum, description, orderNum, quotedPrice
                FROM part_order
                WHERE quotedPrice > 100;"""
query_mysql_executor(query= query2_b, conn=conn)

#c.	Write and execute the query that the DBMS actually executes.
query2_c = """UPDATE part_order SET quotedPrice = 100
                WHERE partNum = 'AT94';"""
query_mysql_executor(query= query2_c, conn=conn)

if conn:
    conn.close()
