import mysql.connector

def query_mysql_executor(query):
    conn = None
    cursor = None
    result = None
    conn = mysql.connector.connect(
        host ='localhost',
        user = 'root',
        password = '8551649',
        database = 'premiere'
    )

    cursor = conn.cursor()
    query = query
    cursor.execute(query)
    result = cursor.fetchall()
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    return result
#1. For each order. list the order number and order date along with the
#   number and name of the customer that placed the order.
query = """SELECT orderNum, orderDate, orders.customerNum, customerName
           FROM orders, customer
           WHERE orders.customerNum = customer.customerNum;"""
print('#1')
result1 = query_mysql_executor(query=query)
print(result1)
#2. For each order placed on October 23, 2010, list the order number along with
#   the number and name of the customer that placed the order.
query = """SELECT orderNum, orders.customerNum, customerName
           FROM orders, customer
           WHERE orders.customerNum = customer.customerNum
           AND orderDate = '2010-10-23';"""
print('#2')
result2 = query_mysql_executor(query=query)
print(result2)
#3. For each order, list the order number, order date, part number, number of
#   units ordered, and quoted price for each order line that makes up the order
query = """SELECT orderline.orderNum, orderDate, partNum, numOrdered, quotedPrice
           FROM orders, orderline
           WHERE orderline.orderNum = orders.orderNum;"""
print('#3')
result3 = query_mysql_executor(query=query)
print(result3)
#4. Use the IN operator to find the number and name of each customer that placed
#   an order on October 23, 2010
query = """SELECT customerNum, customerName
           FROM customer
           WHERE customerNum IN(
                SELECT customerNum FROM orders
                WHERE orderDate = '2010-10-23');"""
print('#4')
result4 = query_mysql_executor(query=query)
print(result4)
