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

# 3 Create a view named order_total. It consists of the order number and order total for each 
# order currently on file. (The order total is the sum of the number of units ordered multiplied by 
# the quoted price on each order line for each order.) Sort the row by order number. Use total_amount 
# as the name for the order total.
# a.	Write and execute the CREATE VIEW command to create the order_total view.
query3_a = """CREATE VIEW order_total
                AS SELECT orderNum, numOrdered * quotedPrice AS total_amount
                FROM orderline
                ORDER BY orderNum;"""
query_mysql_executor(query= query3_a, conn=conn)

# b.	Write and execute the command to retrieve the order number and order total for 
# only those orders totaling more than $1000
query3_b = """SELECT orderNum, total_amount
                FROM order_total
                WHERE total_amount > 1000;"""
query_mysql_executor(query= query3_b, conn=conn)

# c.	Write and execute the query that the DBMS actually executes.
query3_c = """UPDATE order_total
                SET total_amount = 1100
                WHERE orderNum = '21610';"""
query_mysql_executor(query= query3_c, conn=conn)

#Write, but do not execute, the commands to grant th following privileges:
#a.	User Ashton must be able to retrieve data from the part table
query4_a = """CREATE USER 'Ashton'@'localhost' IDENTIFIED BY '123456';
              GRANT SELECT ON part TO 'Ashton'@'localhost';"""
query_mysql_executor(query= query4_a, conn=conn)

#b.	Users Kelly and Morgan must be able to add new orders and order lines.
query4_b = """CREATE USER 'Kelly'@'localhost' IDENTIFIED BY '12345',
                          'Morgan'@'localhost' IDENTIFIED BY '1234';
              GRANT SELECT, INSERT ON orderline TO Kelly'@'localhost', 'Morgan'@'localhost';"""
query_mysql_executor(query= query4_b, conn=conn)

#c.	User James must be able to change the price for all parts
query4_c = """CREATE USER 'James'@'localhost' IDENTIFIED BY '654321';
              GRANT SELECT, UPDATE ON part TO 'James'@'localhost';"""
query_mysql_executor(query= query4_c, conn=conn)

#d.	User Danielson must be able to delete customers.
query4_d = """CREATE USER 'Danielson'@'localhost' IDENTIFIED BY '54321';
              GRANT SELECT, DELETE ON customer TO 'Danielson'@'localhost';"""
query_mysql_executor(query= query4_d, conn=conn)

#e.	All users must ba able to retrieve each customer’s number, name, street, city, state, and zip code.
query4_e = """GRANT SELECT(customerNum, customerName, street, city, state, zip)
                ON customer
                TO PUBLIC;"""
query_mysql_executor(query= query4_e, conn=conn)

#f.	User Perez must be able to create an index on the orders table
query4_f = """CREATE USER 'Perez'@'localhost' IDENTIFIED BY '4321';
              GRANT INDEX ON orders TO 'Perez'@'localhost';"""
query_mysql_executor(query= query4_f, conn=conn)

#g.	User Washington must be able to change the structure of the part table
query4_g = """CREATE USER 'Washington'@'localhost' IDENTIFIED BY '321';
              GRANT ALTER ON part TO 'Washington'@'localhost';"""
query_mysql_executor(query= query4_g, conn=conn)

#h.	User Grinstead must have all privileges on the orders table
query4_h = """CREATE USER 'Grinstead'@'localhost' IDENTIFIED BY '112233';
              GRANT ALL ON orders TO 'Grinstead'@'localhost';"""
query_mysql_executor(query= query4_h, conn=conn)

#Write, but do not execute the command to revoke all privileges from user Ashton.
query5 = """REVOKE SELECT ON part FROM 'Ashton'@'localhost';"""
query_mysql_executor(query= query5, conn=conn)

#6 Perform the following task:
#a.	Create an index named part_index1 on the part_num column in the order_line table
query6_a = """CREATE INDEX part_index1 ON orderline(partNum);"""
query_mysql_executor(query= query6_a, conn=conn)

#b.	Create an index named part_index2 on the class column in the part table.
query6_b = """CREATE INDEX part_index2 ON part(class);"""
query_mysql_executor(query= query6_b, conn=conn)

#c.	Create an index named part_index3 on the class and warhouse columns in 
# the part table. 
query6_c = """CREATE INDEX part_index3 ON part(class, warehouse);"""
query_mysql_executor(query= query6_c, conn=conn)

#d.	Create an index named part_index4 on the class and warehouse columns in 
# the part table. List item classes in descending order.
query6_d = """CREATE INDEX part_index4 ON part(class, warehouse);
             SELECT class FROM part ORDER BY class DESC;"""
query_mysql_executor(query= query6_d, conn=conn)

#7 Delete the index named part_index3
query7 = """DROP INDEX part_index3 ON part;"""
query_mysql_executor(query= query7, conn=conn)

#8 Write the commands to obtain the following information from the system catalog. 
# Do not execute these commands unless your instructor asks you to do so.
#a.	List every table that contains a column named customer_num
query8_a = """SELECT TABLE_NAME
              FROM INFORMATION_SCHEMA.COLLUMNS
              WHERE COLUMN_NAME = 'customerNum';"""
query_mysql_executor(query= query8_a, conn=conn)

#b.	List every column in the part table and lits associated data type.
query8_b = """SHOW COLUMNS FROM part;"""
query_mysql_executor(query= query8_b, conn=conn)

#9 Add the order_num column as a foreign key in the order_line table
query9 = """ALTER TABLE orderline
            ADD CONSTRAIN fk_orderNum
            FOREIGN KEY(orderNum) REFERENCES orders(orderNum);"""
query_mysql_executor(query= query9, conn=conn)


if conn:
    conn.close()
