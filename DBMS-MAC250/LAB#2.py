import mysql.connector

conn = mysql.connector.connect(
    host ='localhost',
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
        return result
    except Exception as e:
        raise Exception('Query failed %s', e)
    
#1. For each order. list the order number and order date along with the
#   number and name of the customer that placed the order.
query = """SELECT orderNum, orderDate, orders.customerNum, customerName
           FROM orders, customer
           WHERE orders.customerNum = customer.customerNum;"""
print('#1')
result1 = query_mysql_executor(query=query, conn=conn)
print(result1)
#2. For each order placed on October 23, 2010, list the order number along with
#   the number and name of the customer that placed the order.
query = """SELECT orderNum, orders.customerNum, customerName
           FROM orders, customer
           WHERE orders.customerNum = customer.customerNum
           AND orderDate = '2010-10-23';"""
print('#2')
result2 = query_mysql_executor(query=query, conn=conn)
print(result2)
#3. For each order, list the order number, order date, part number, number of
#   units ordered, and quoted price for each order line that makes up the order
query = """SELECT orderline.orderNum, orderDate, partNum, numOrdered, quotedPrice
           FROM orders, orderline
           WHERE orderline.orderNum = orders.orderNum;"""
print('#3')
result3 = query_mysql_executor(query=query, conn=conn)
print(result3)
#4. Use the IN operator to find the number and name of each customer that placed
#   an order on October 23, 2010
query = """SELECT customerNum, customerName
           FROM customer
           WHERE customerNum
           IN(SELECT customerNum FROM orders
                WHERE orderDate = '2010-10-23');"""
print('#4')
result4 = query_mysql_executor(query=query, conn=conn)
print(result4)
#7. For each order, list the order number, order date, part number, part description
#   and item class for each part that makes up the order.
query = """SELECT orderNum, orderDate, partNum, description, class
           FROM orders, part;"""
print('#7')
result7 = query_mysql_executor(query=query, conn=conn)
print(result7)
#8. Repeat Exercise 7, but this time order the rows by item class and then by order number.
query = """SELECT orderNum, orderDate, partNum, description, class
           FROM orders, part
           ORDER BY class, orderNum;"""
print('#8')
result8 = query_mysql_executor(query=query, conn=conn)
print(result8)
#11.Find the number and name of each customer that currently has an order on 
#   file for a Gas Range.
query = """SELECT customer.customerNum, customerName
           FROM customer, orders, orderline, part
           WHERE customer.customerNum = orders.customerNum
           And orders.orderNum = orderline.orderNum
           ANd orderline.partNum = part.partNum
           ANd description = 'Gas Range';"""
print('#11')
result11 = query_mysql_executor(query=query, conn=conn)
print(result11)
#12.List the part number, part description, and item class for each pair of parts that are in
#   the same item class.
query = """SELECT partNum, description, class FROM part
           ORDER BY class;"""
print('#12')
result12 = query_mysql_executor(query=query conn=conn,)
print(result12)
#13.List the order number and order date for each order placed by the customer named
#   Johnson's Department Store
query = """SELECT 0.orderNum, orderDate
           FROM orders o, customer c
           WHERE o.customerNum = c.customerNum
           AND customerName = 'Johnson''s Department Store';"""
print('#13')
result13 = query_mysql_executor(query=query, conn=conn)
print(result13)
#14.List the order number and order date for each order that contains an order line for an Iron
query = """SELECT o.orderNum, orderDate
           FROM orders o, orderline l, part p
           WHERE o.orderNum = l.orderNum
           AND l.partNum = p.partNum
           AND description = 'Iron';"""
print('#14')
result14 = query_mysql_executor(query=query, conn=conn)
print(result14)

if conn:
    conn.close()
