import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user='root',
    password="8551649",
    database="practicebase"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS practicebase")

cursor.execute("CREATE TABLE IF NOT EXISTS person (id INT PRIMARY KEY, name VARCHAR(64))")
cursor.execute("CREATE TABLE IF NOT EXISTS thing (id INT PRIMARY KEY, name VARCHAR(64))")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS owns (
    person INT,
    things INT,
    FOREIGN KEY (person) REFERENCES person (id),
    FOREIGN KEY (thing) REFERENCES thing (id));
""")

conn.commit()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

cursor.execute("""
    INSERT INTO person (id, name) VALUES
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Charlie');
""")

cursor.execute("""
    INSERT INTO thing (id, name) VALUES
    (1, 'Apple'),
    (2, 'Box'),
    (3, 'Computer');
""")

cursor.execute("""
    INSERT INTO owns (person, thing) VALUES
    (2, 1),
    (2, 3),
    (1, 2); 
""")
conn.commit()
cursor.close()
conn.close()
