import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees(
        first name 
        last name
        pay
        )""")

conn.commit()

conn.close()
