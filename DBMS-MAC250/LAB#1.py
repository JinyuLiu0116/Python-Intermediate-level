import mysql.connector

def query_mysql_executor(query):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '8551649',
            database = 'premiere'
        )
        if conn:
            print('Connection has been built')

        cursor = conn.cursor()
        if cursor:
            print('Cursor has been built')
    except Exception as e:
        raise Exception(f"Job Failed {e}")
    
    finally:
        if cursor:
            cursor.close()
            print('Cursor has been closed')
        if conn:
            conn.close()
            print('Connection has been closed')

    #List the part number, description, and price for part.
    query = 'SELECT partNum, description, price FROM part'
    cursor.execute(query)
    
    result = cursor.fetchall()
    print('#1')
    for row in result:
        print(row)

    #2.List all rows and columns for the complete orders table
    query = 'SELECT * FROM orders;'
    cursor.execute(query)
    result = cursor.fetchall()
    print('#2')
    for row in result:
        print(row)
        
    #3.List the names of customers with credit limits of $10,000 or more.
    query = 'SELECT customerName FROM customer WHERE creditLimit >= 10000;'
    cursor.execute(query)
    result = cursor.fetchall()
    print('#3')
    for row in result:
        print(row)
        
    #4.List the order number for each placed by customer number 608 on 10/23/2010
    query = """SELECT orderNum FROM orders 
            WHERE customerNum = 608 AND orderDate = '2010-10-23';"""
    cursor.execute(query)
    result = cursor.fetchall()
    print('#4')
    for row in result:
        print(row)

    #5.List the number and name of each customer represented by sales rep 35 or sales rep 65
    query = """
                SELECT customerNum, customerName FROM customer
                WHERE repNum = '35' OR repNum = '65';
            """
    cursor.execute(query)
    result = cursor.fetchall()
    print('#5')
    for row in result:
        print(row)
    
    #6.List the part number and part description of each part that is not in item class AP
    query = """SELECT partNum, description FROM part WHERE class != 'AP';"""
    cursor.execute(query)
    result = cursor.fetchall()
    print('#6')
    for row in result:
        print(row)

    #7.List the part number, description, and number of units on hand for each part that
    #  has between 10 and 25 units on hand, including both 10 and 25. Do this in two ways
    query1 = """SELECT partNum, description, onHand FROM part WHERE onHand BETWEEN 10 AND 25;"""
    query2 = """
                Select partNum, description, onHand FROM part
                WHERE onHand >= 10 AND onHand <= 25;
             """
    print('#7')
    cursor.execute(query1)
    result1 = cursor.fetchall()
    for row in result1:
        print(row)

    cursor.execute(query2)
    result2 = cursor.fetchall()
    for row in result2:
        print(row)
    
    #8.List the part number, part description, and on hand value of each part in item class SG
    #  Assign the name ON_HAND_VALUE to the computed column.
    query = """SELECT partNum, description, onHand * price AS ON_HAND_VALUE
               FROM part WHERE class = 'SG';"""
    cursor.execute(query)
    result = cursor.fetchall()
    print('#8')
    for row in result:
        print(row)
    
    #9.List the part number, part description, and onhand value for each part whose on hand
    #  value is ate least$7,500. 
    query = """SELECT partNum, description, onHand * price AS ON_HAND_VALUE
               FROM part WHERE onHand * price >= 7500;"""
    cursor.execute(query)
    result = cursor.fetchall()
    print('#9')
    for row in result:
        print(row)

    #10.Use the IN operator to list the part number and part description of each part in item class
    #   AP or SG
    query = """SELECT partNum, description FROM part
               WHERE class IN('AP', 'SG');"""
    cursor.execute(query)
    result = cursor.fetchall()
    print('#10')
    for row in result:
        print(row)
    
    #11.Find the number and name of each customer whose name begins with the letter"B"
    query = """SELECT customerNum, customerName FROM customer
               WHERE customerName LIKE 'B%';"""
    cursor.execute(query)
    result = cursor.fetchall()
    print('#10')
    for row in result:
        print(row)

    #12.List all details about all parts. Order the output by part description
    query = """SELECT * FROM part ORDER BY description;"""
    cursor.execute(query)
    result = cursor.fetchall()
    print('#12')
    for row in result:
        print(row)

    #13.List all details about all parts. order the output by part number
    #   within warehouse(That is, order the output by warehouse and the by part number)
    query = """SELECT * FROM part ORDER BY warehouse, partNum;"""
    cursor.execute(query)
    print('#13')
    for row in cursor.fetchall():
        print(row)
    
    #14.How many customers have balances that are more than their credit limits?
    query = """SELECT COUNT(*) FROM customer
               WHERE balance > creditLimit;"""
    cursor.execute(query)
    print('#14')
    for row in cursor.fetchall():
        print(row)

    #15.Find the total of the balances for all customers represented by sales
    #   rep 65 with balances that are less than their credit limits
    query = """SELECT SUM(balance) FROM customer
               WHERE repNum = '65'
               AND balance < creditLimit;"""
    cursor.execute(query)
    print('#15')
    for row in cursor.fetchall():
        print(row)
