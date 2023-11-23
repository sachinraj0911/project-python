import sqlite3

conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()
# c.execute("CREATE TABLE IF NOT EXISTS employee1(fname text,lname text,pay real)")
# c.execute("INSERT INTO employee1 VALUES('SACHIN','KUMAR',45000)")
c.execute("INSERT INTO employee1 VALUES('RAJ','KUMAR',47000)")
# c.execute("delete from employee1")
conn.commit()
# c.execute("SELECT *FROM employee1")
c.execute("SELECT *FROM employee1 WHERE pay = 45000")
a=c.fetchall()
for i in a:
    print(i)


c.close()
conn.close()
