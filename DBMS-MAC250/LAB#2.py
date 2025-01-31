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
    if conn:
        print('Connection has been built')
    
    cursor = conn.cursor()
    if cursor:
        print('Cursor has been created')

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
result = query_mysql_executor(query)
print(result)
