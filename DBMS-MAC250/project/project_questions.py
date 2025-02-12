import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'doctor'
)

def query_mysql_executor(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Query failed at {e}")

#Print all INS records for State = “NY” 
query = """SELECT * FROM ins WHERE state = 'NY';"""
print(f"#1: {query_mysql_executor(query=query,conn=conn)}")

#Print the cpt (Mp_code) record that has the highest price
query2 = """SELECT * FROM medical WHERE price = (SELECT MAX(price) FROM medical);"""
print(f"#2: {query_mysql_executor(query=query2,conn=conn)}")

#Print the name of the patient that has the most treatments (# of records in the treatments file) 
query3 = """SELECT p_name FROM patients WHERE p_code IN 
                (SELECT p_code FROM treatments GROUP BY p_code HAVING COUNT(p_code) = 
                    (SELECT MAX(t_count) FROM (SELECT COUNT(p_code) AS t_count 
                        FROM treatments GROUP BY p_code)AS subquery));"""
print(f"#3: {query_mysql_executor(query=query3,conn=conn)}")
