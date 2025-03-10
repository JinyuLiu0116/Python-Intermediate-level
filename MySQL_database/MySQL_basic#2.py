import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "8551649",
    database = "practice"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS practice")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS movie(
    Id INT PRIMARY KEY,
    Title VARCHAR(64),
    Director VARCHAR(64),
    Year INT,
    Length_minutes INT);
""")

cursor.execute("""
    INSERT INTO movie(Id, Title, Director, Year, Length-minutes) VALUES
    (1, 'Toy Story', 'John Lasseter', 1995, 81),
    (2, 'A Bug''s Life', 'John Lasseter', 1998, 95),
    (3,	'Toy Story 2', 'John Lasseter',	1999, 93),
    (4,	'Monsters, Inc.', 'Pete Docter', 2001, 92),
    (5,	'Finding Nemo',	'Andrew Stanton', 2003, 107),
    (6,	'The Incredibles', 'Brad Bird',	2004, 116),
    (7,	'Cars',	'John Lasseter', 2006, 117),
    (8,	'Ratatouille', 'Brad Bird', 2007, 115),
    (9,	'WALL-E', 'Andrew Stanton', 2008, 104),
    (10, 'Up', 'Pete Docter', 2009, 101),
    (11, 'Toy Story 3',	'Lee Unkrich', 2010, 103),
    (12, 'Cars 2', 'John Lasseter', 2011, 120),
    (13, 'Brave', 'Brenda Chapman', 2012, 102),
    (14, 'Monsters University', 'Dan Scanlon', 2013, 110);
""")
conn.commit()
cursor.execute("SELECT * FROM movie")
result = cursor.fetchall()
for i in result:
    print(i)

if cursor:
    cursor.close()
if conn:
    conn.close()
