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
# b) List the names of all employees who have a dependent with the same first name as themselves. 
query2 = """
        SELECT f_name, m_name, l_name
        FROM employee e, dependent d
        WHERE e.e_ssn = d.e_ssn
        AND e.f_name = d.dependent_name;
        """
cursor = conn.cursor()
cursor.execute(query2)
result2 = cursor.fetchall()

for row in result2:
    print(row)
# c) Find the names of all employees who are directly supervised by ‘Franklin Wong’. 
query3 = """
        SELECT f_name, m_name, l_name
        FROM employee
        WHERE sup_e_ssn = (
                            SELECT e_ssn FROM employee
                            WHERE f_name = 'Franklin'
                            AND l_name = 'Wong');
        """
cursor = conn.cursor()
cursor.execute(query3)
result3 = cursor.fetchall()

for row in result3:
    print(row)
