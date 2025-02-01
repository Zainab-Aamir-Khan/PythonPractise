import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXITS employees(
#         first_name TEXT, 
#         last_name TEXT,
#         pay INTEGER
#         )""")

c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)")

conn.commit()

c.execute("SELECT * FROM employees WHERE last_name= 'Schafer'")

print(c.fetchall())

conn.commit()

conn.close()
