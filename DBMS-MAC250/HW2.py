import mysql.connector

def query_mysql_executor(query):
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '8551649',
        database = 'company'
    )
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        raise Exception('Query failed %s', e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

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
result = query_mysql_executor(query)
print(f"#1: {result}")

# b) List the names of all employees who have a dependent with the same first name as themselves. 
query2 = """
        SELECT f_name, m_name, l_name
        FROM employee e, dependent d
        WHERE e.e_ssn = d.e_ssn
        AND e.f_name = d.dependent_name;
        """
result2 = query_mysql_executor(query2)
print(f"#2: {result2}")
# c) Find the names of all employees who are directly supervised by ‘Franklin Wong’. 
query3 = """
        SELECT f_name, m_name, l_name
        FROM employee
        WHERE sup_e_ssn = (
                            SELECT e_ssn FROM employee
                            WHERE f_name = 'Franklin'
                            AND l_name = 'Wong');
        """
result3 = query_mysql_executor(query3)
print(f"#3: {result3}")
# d) For each project, list the project name and the total hours per week (by all employees) spent on that project. 
query4 = """
        SELECT p_name, SUM(hours) as total_hours
        FROM project p, works_on w
        WHERE p.p_num = w.p_num
        GROUP BY p_name;"""

result4 = query_mysql_executor(query4)
print(f"#4: {result4}")
# e) For each department, retrieve the department name and the average salary of all employees working in that department.
query5 = """SELECT d_name, AVG(salary) as avg_salary
            FROM department d, employee e
            WHERE d.d_num = e.d_num
            GROUP BY d_name;""" 
result5 = query_mysql_executor(query5)
print(f"#5: {result5}")   
# f) Retrieve the name of employees who work on EVERY project. 
query6 = """SELECT f_name, m_name, l_name AS name
            FROM employee e
            WHERE e.e_ssn =(SELECT e_ssn FROM works_on GROUP BY e_ssn HAVING COUNT(p_num) = (
		        SELECT COUNT(p_num) FROM project));"""

result6 = query_mysql_executor(query6)
print(f"#6: {result6}")
#g) Retrieve the average salary of all female employees. 
query7 ="""SELECT AVG(salary) FROM employee
            WHERE sex = 'M';"""
result7 = query_mysql_executor(query7)
print(f"#7: {result7}")
# h) Find the names and addresses of all eemployees who work on at least one project located in Houston, 
# but whose department has no location in Houston. 
query8 = """SELECT f_name, m_name, l_name, address
            FROM employee e, dept_locations d, project p, works_on w
            WHERE e.e_ssn = w.e_ssn
            AND w.p_num = p.p_num
            AND p.d_num = d.d_num
            AND w.hours IS NOT Null
            AND p.p_location = 'HOUSTON'
            AND d.d_location != 'HOUSTON'
            GROUP BY f_name, m_name, l_name, address;"""
result8 = query_mysql_executor(query8)
print(f"#8: {result8}")
# i) List the last names of all department managers who have no dependents.
query9 = """SELECT l_name
            FROM employee
            WHERE e_ssn IN
            (SELECT mgr_ssn FROM department
             WHERE mgr_ssn NOT IN
                (SELECT e_ssn FROM dependent));"""
result9 = query_mysql_executor(query9)
print(f"#9: {result9}")
