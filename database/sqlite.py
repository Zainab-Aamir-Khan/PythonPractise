import sqlite3

conn = sqlite3.connet('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees""")