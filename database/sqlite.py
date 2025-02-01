import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees(
#         first name 
#         last name
#         pay
#         )""")

c.execute("SELECT * FROM employees WHERE last= 'schafer'")

conn.commit()

conn.close()
