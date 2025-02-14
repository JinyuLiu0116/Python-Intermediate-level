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
        return result
    except Exception as e:
        print(f"Query failed at: {e}")
query1 = """CREATE TABLE nonappliance(
            partNum CHAR(4) PRIMARY KEY,
            description CHAR(15),
            onHand DECIMAL(4,0),
            class CHAR(2),
            price DECIMAL(6,2));"""
print(f"#1: {query_mysql_executor(query=query1, conn=conn)}")

# Insert into the nonappliance table the part number, part description, number of units on hand, item class,
# and unti price from the PART table for each part that is not in item class AP
query2 = """INSERT INTO nonappliance SELECT partNum, description, onHand, class, price FROM part WHERE class != 'AP';"""
print(f"#2: {query_mysql_executor(query=query2, conn=conn)}")

#In the nonappliance table, change the description oof part number AT94 to “Steam Iron”
query3 = """UPDATE nonappliance SET description = 'Steam Iron'
            WHERE partNum ='AT94';"""
print(f"#3: {query_mysql_executor(query=query3, conn=conn)}")

#4 In the noappliance table, increase the price of each item in item class ‘SG’ by three percent.
query4 = """UPDATE nonappliance SET price = price * 1.05 WHERE class = 'SG';"""
print(f"#4: {query_mysql_executor(query=query4, conn=conn)}")

#5.Add the following part to the nonappliance table: part number: TL92; 
#description: Edge Trimmer, number of units on hand: 11, class HW, and price 29.95
query5 = """INSERT INTO nonappliance VALUES
            ('TL92', 'Edge Trimmer', 11, 'HW', 29.95);"""
print(f"#5: {query_mysql_executor(query=query5, conn=conn)}")

#6.Delete every part in the nonappliance table for which the class is ‘SG’
query6 = """DELETE FROM nonappliance WHERE class = 'SG';"""
print(f"#6: {query_mysql_executor(query=query6, conn=conn)}")
