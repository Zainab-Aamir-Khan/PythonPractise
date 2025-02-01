import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXITS employees(
#         first_name TEXT, 
#         last_name TEXT,
#         pay INTEGER
#         )""")

emp_1 = Employee('john','Doe',80000)
emp_2 = Employee('jane','Doe',70000)

print(emp_1.first)
print(emp_1.last )
print(emp_1.pay)