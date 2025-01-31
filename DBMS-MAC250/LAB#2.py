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
result1 = query_mysql_executor(query)
print(result1)
#2. For each order placed on October 23, 2010, list the order number along with
#   the number and name of the customer that placed the order.
query = """SELECT orderNum, orders.customerNum, customerName
           FROM orders, customer
           WHERE orders.customerNum = customer.customerNum
           AND orderDate = '2010-10-23';"""
print('#2')
result2 = query_mysql_executor(query)
print(result2)
