import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'doctor'
)

def query_mysql_executor(query, conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
        conn.commit()   
    except Exception as e:
        print(f"query is failed at:{e}")
    
query1 = """INSERT INTO ins VALUES
            ('GHI', 'Group Health Insurance', '11-11 11th st', 'Longisland City','NY','11101'),
            ('BC', 'Blue Cross', '22-22 22th st', 'Sunnyside','NY','11102'),
            ('AHS', 'American Health System', '33-33 33th st', 'Woodside','NY','11103');"""
query_mysql_executor(query=query1,conn=conn)

query2 = """INSERT INTO patients VALUES
            ('P1','Frank Liu','GHI','10-10 10th st','Apt 1A','Longisland City','NY','11101'),
            ('P2','Rosi Liu','BC','20-20 20th st','Apt 2B','Sunnyside','NY','11102'),
            ('P3','Alex Liu','BC','30-30 30th st','Apt 3C','Woodside','NY','11103'),
            ('P4','Albert Liu','BC','40-40 40th st','Apt 4D','Elmhurst','NY','11104'),
            ('P5','Sue Liu','GHI','50-50 50th st','Apt 5E','Jackson Heights','NY','11105'),
            ('P6','Richard Liu','AHS','60-60 60th st','Apt 6F','Flushing','NY','11106');"""
query_mysql_executor(query=query2,conn=conn)

query3 = """INSERT INTO mds VALUES
            ('M1','Dr.Anthony Liu','41-41 44th Ave','Longisland City','NY','11101'),
            ('M2','Dr.Jack Liu','62-62 45th Ave','longisland City','NY','11101'),
            ('M3','Dr.Jane Liu','112-26 37th Ave','Elmhurst','NY','11104'),
            ('M4','Dr.Louis Liu','100-30 Main st','Flushing','NY','11106'),
            ('M5','Dr.Kate Liu','122-40 Main st','Flushing','NY','11106');"""
query_mysql_executor(query=query3,conn=conn)

query4 = """INSERT INTO medical VALUES
            ('1111','Throat culture',1.11),
            ('2222','Routine blood test',2.22),
            ('3333','Ingrown toenail removal',3.33),
            ('4444','Fill a cavity',4.44),
            ('5555','Dental x-ray',5.55),
            ('6666','Dental cleaning',6.66),
            ('7777','Nose bleed treatment',7.77),
            ('8888','Splinter removal',8.88);"""
query_mysql_executor(query=query4,conn=conn)

if conn:
    conn.close()
