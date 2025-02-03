import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'company'
)

#a) Retrieve the names of all employees in Department 5 who work more than 10 hours per week on the ‘Product X’ project. 
query = """
        SELECT f_name, m_name, l_name
        FROM employee e, department d, project p, works_on w
        WHERE e.e_ssn = w.e_ssn
        AND w.p_num = p.p_num
        AND p.d_num = d.d_num
        AND d.d_num = '5'
        AND hours > 10
        AND p.p_name = 'productx';"""
cursor = conn.cursor()
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)
