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
        print("--------------------------------------------------------------------")
    except Exception as e:
        print(f"query failed: {e}")

# Use the Premiere Products database to complete the following exercises.
# If directed to do so by your instructor, use the information provided with
# Exercises to print your output

# 1.List the part number and description for all parts. The part descriptions
# should appear in uppercase letters.
query1 = """SELECT partNum, UPPER(description) FROM part;"""
query_mysql_executor(query=query1, conn=conn)

# 2.List the customer number and name for all customers located in the
# city of Grove. Your query should ignore case. For example, a customer with th
# city Grove should be included as should customers whose city is GROVE, grove, GrOvE, and so on
query2 = """SELECT customerNum, customerName FROM customer WHERE city LIKE 'grove';"""
query_mysql_executor(query=query2, conn=conn)

# 3.List the customer number, name, and balance for all customers. The balance
# should be rounded to the nearest dollar.
query3 = """SELECT customerNum, customerName, ROUND(balance) FROM customer;"""
query_mysql_executor(query=query3, conn=conn)

# 4.Premiere Products is running a promotion that is valid for up to 20 days after
# an order is placed. List the order number, customer number, customer name,
# and the promotion date for each order. The promotion date is 20d days after the order was placed.
query4 = """SELECT o.orderNum, c.customerNum, c.customerName, DATE_ADD(o.orderDate, INTERVAL 20 DAY) AS promotionDate
            FROM customer c, orders o
            WHERE c.customerNum = o.customerNum;"""
query_mysql_executor(query=query4, conn=conn)

# 5.Write the code for the following triggers in PL/SQL or T-SQL following the style shown in the text:
# a. When adding a customer, add the customer’s balance times the sales rep’s commission rate to 
# the commission for the corresponding sales rep.
query5_a = """CREATE TRIGGER sales_rep
                AFTER INSERT ON customer
                FOR EACH ROW
                UPDATE rep
                SET commission = commission + (NEW.balance * rate)
                WHERE repNum = NEW.repNum;"""
query_mysql_executor(query=query5_a, conn=conn)
query_insert_data = """INSERT INTO customer VALUES ('111','JoJo Seriey','1111 Berger','New York City','NY','11111',5000,5000,20);"""

# b. When updating a customer, add the difference between the new balance and the old balance 
# multipled by the sales rep’s commission rate to the commission for the corresponding sales rep.
query5_b = """CREATE TRIGGER different_commission
                AFTER UPDATE ON customer
                FOR EACH ROW
                UPDATE rep
                SET commission = commission + ((NEW.balance - OLD.balance) * rate)
                WHERE repNum = NEW.repNum;"""
query_mysql_executor(query=query5_b, conn=conn)
query_update_data = """UPDATE customer SET balance = 3000 WHERE customerNum = '111';"""

# c. When deleting a customer, subtract the balance multiplied by the sales rep’s commission 
# rate from the commission for the corresponding sales rep.
query5_c = """CREATE TRIGGER multiply_commission
                AFTER DELETE ON customer
                FOR EACH ROW
                UPDATE rep
                SET commission = commission - OLD.balance * rate
                WHERE repNum = OLD.repNum;"""
query_mysql_executor(query=query5_c, conn=conn)
query_delete_data = """DELETE FROM customer WHERE customerNum = '111';"""
