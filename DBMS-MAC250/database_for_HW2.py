conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'company'
)

query = """CREATE TABLE employee(
            f_name CHAR(30),
            m_name CHAR(1),
            l_name CHAR(30),
            e_ssn CHAR(9),
            date DATE,
            address CHAR(50),
            salary INT,
            sup_e_ssn CHAR(9),
            d_num CHAR(1)
            );"""

query = """ALTER TABLE employee
            ADD CONSTRAINT pk_employee
            PRIMARY KEY(e_ssn);"""


query = """CREATE TABLE department(
            d_name CHAR(30),
            d_num CHAR(1) PRIMARY KEY,
            mgr_ssn CHAR(9),
            mgr_start_date DATE);"""

query = """ALTER TABLE employee
            ADD CONSTRAINT fk_employee
            FOREIGN KEY(d_num)
            REFERENCES department(d_num);"""
cursor = conn.cursor()
cursor.execute(query)
