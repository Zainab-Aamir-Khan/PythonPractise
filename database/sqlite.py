import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS employees")


# c.execute("""CREATE TABLE employees(
#         first_name TEXT, 
#         last_name TEXT,
#         pay INTEGER
#         )""")

c.execute("INSERT INTO employees  (first_name, last_name, pay) VALUES ('Corey', 'Schafer', 50000)")

conn.commit()


c.execute("SELECT * FROM employees WHERE last_name= 'Schafer'")

print(c.fetchone())


conn.close()
