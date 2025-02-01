import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees(
#         first name 
#         last name
#         pay
#         )""")

# c.execute(INSERT INTO employees VALUES ("Corey", "Schafer", 50000))

c.execute("SELECT * FROM employees WHERE last= 'Schafer'")

# c.fetchmany(5)
print(c.fetchone())
# c.fetchall()

conn.commit()

conn.close()
