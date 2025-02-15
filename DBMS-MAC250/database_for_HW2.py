import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'company'
)

def query_mysql_executor(query, conn):
    
query = """CREATE TABLE department(
            d_name CHAR(30),
            d_num CHAR(1) PRIMARY KEY,
            mgr_ssn CHAR(9),
            mgr_start_date DATE);"""

query = """CREATE TABLE employee(
            f_name CHAR(30),
            m_name CHAR(1),
            l_name CHAR(30),
            e_ssn CHAR(9) PIRMARY KEY,
            date DATE,
            address CHAR(50),
            sex CHAR(1),
            salary DECIMAL(6,2),
            sup_e_ssn CHAR(9),
            d_num CHAR(1),
            FOREIGN KEY(d_num) REFERENCES department(d_num)
            );"""

query ="""
        CREATE TABLE dept_locations(
        d_num  CHAR(1),
        d_location CHAR(15),
        PRIMARY KEY(d_num, d_location));"""

query = """
        ALTER TABLE dept_locations
        ADD CONSTRAINT fk_location_department
        FOREIGN KEY(d_num) REFERENCES department(d_num);"""

query = """
        CREATE TABLE project(
        p_name CHAR(30),
        p_num CHAR(2) PRIMARY KEY,
        p_location CHAR(20),
        d_num CHAR(1),
        FOREIGN KEY(d_num) REFERENCES dept_locations(d_num));"""

query = """
        CREATE TABLE works_on(
        e_ssn CHAR(9),
        p_num CHAR(2),
        hours DECIMAL(4,2),
        PRIMARY KEY(e_ssn, p_num));"""

query = """
        ALTER TABLE works_on
        ADD CONSTRAINT fk_works_e
        FOREIGN KEY(e_ssn) REFERENCES employee(e_ssn),
        ADD CONSTRAINT fk_works_project
        FOREIGN KEY(p_num) REFERENCES project(p_num);"""

query = """
        CREATE TABLE dependent(
        e_ssn CHAR(9),
        dependent_name CHAR(15),
        sex CHAR(1),
        date DATE,
        relationship CHAR(15),
        PRIMARY KEY(e_ssn, dependent_name),
        FOREIGN KEY(e_ssn) REFERENCES employee(e_ssn)
        );"""

cursor = conn.cursor()
cursor.execute(query)




if cursor:
    cursor.close()
if conn:
    conn.close()
