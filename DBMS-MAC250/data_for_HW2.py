import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'company'
)
# query = "ALTER TABLE employee MODIFY COLUMN salary DECIMAL(6,0);"
query = """
        INSERT INTO employee VALUES
        ('JOHN','B','SMITH','123456789','1965-01-09','731 FONDREN, HOUSTON, TX','M',30000,'333445555','5'),
        ('FRANKLIN','T','WONG','333445555','1955-12-08','638 VOSS, HOUSTON, TX','M',40000,'888665555','5'),
        ('ALICIA','J','ZELAYA','999887777','1968-07-19','3321 CASTLE, SPRING, TX','F',25000,'987654321','4'),
        ('JENNIFER','S','WALLACE','987654321','1941-06-20','291, BERRY, BELLAIRE, TX','F',43000,'888665555','4'),
        ('RAMESH','K','NARAYAH','666884444','1962-09-15','975 FIRE OAK, HUMBLE, TX','M',38000,'333445555','5'),
        ('JOYCE','A','ENGLISH','453453453','1972-07-31','5631, RICE, HOUSTON, TX','F',25000,'333445555','5'),
        ('AHMAD','V','JABBAR','987987987','1969-03-29','980, DALLAS, HOUSTON, TX','M',25000,'987654321','4'),
        ('JAMES','E','BORG','888665555','1937-11-10','450 STONE, HOUSTON, TX','M',55000,'','1');"""
cursor = conn.cursor()
cursor.execute(query)







if cursor:
    cursor.close()
if conn:
    conn.close()
