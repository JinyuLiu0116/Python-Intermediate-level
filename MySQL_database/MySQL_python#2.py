import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="8551649",
    database="stock_data"
)

mycursor=db.cursor()
mycursor.execute("""
                 CREATE TABLE AMZ(
                 Date VARCHAR(10) PRIMARY KEY,
                 Open FLOAT,
                 High FLOAT,
                 Low FLOAT,
                 Close FLOAT,
                 `Adj Close` FLOAT,
                 Volume INT
                 )""")# to keep the space between Adj Close, need to use ``.


mycursor.execute("DESCRIBE amz")

for x in mycursor:
    print(x) #x is iterator obj, will print line by line of mycursor

# how to add element to our table
mycursor.execute("""
                 INSERT INTO amz (Date, Open, High, Low, Close, `Adj Close`, Volume)
                  VALUES (%s,%s,%s,%s,%s,%s,%s)
                 """,("2024-07-30",100.00,110.00,90.00,105.00,100.00,2321453))
db.commit()

mycursor.execute("DESCRIBE amz")
for x in mycursor:
    print(x)