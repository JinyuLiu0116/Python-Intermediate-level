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
# d) For each project, list the project name and the total hours per week (by all employees) spent on that project. 
query4 = """
        SELECT p_name, SUM(hours) as total_hours
        FROM project p, works_on w
        WHERE p.p_num = w.p_num
        GROUP BY p_name;"""

cursor = conn.cursor()
cursor.execute(query4)
result4 = cursor.fetchall()

for row in result4:
    print(row)
# e) For each department, retrieve the department name and the average salary of all employees working in that department.
query5 = """SELECT d_name, AVG(salary) as avg_salary
            FROM department d, employee e
            WHERE d.d_num = e.d_num
            GROUP BY d_name;""" 
cursor = conn.cursor()
cursor.execute(query5)
result5 = cursor.fetchall()

for row in result5:
    print(row)
