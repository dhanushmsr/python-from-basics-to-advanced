import pymysql


connect=pymysql.connect(user='root',password='root',port=3306,host='localhost')

cursor=connect.cursor()

'''cursor.execute('create database emp')
print('database created successfully')'''

'''cursor.execute('create table emp.emp_det(id int(3),name varchar(10),age int(2))')
print('table create successfully')'''

'''cursor.execute("insert into emp.emp_det(id,name,age) value(101,'dhanush',21)")
print(cursor.rowcount,"row created successfully")
cursor.execute("commit")'''

'''val=[
    (102,'aswin',23),
    (103,'Abhi',20),
    (104,'Vetri',25),
    (105,'TVK',1)
]

qry="insert into emp.emp_det(id,name,age) values (%s,%s,%s)"

cursor.executemany(qry,val)
print(cursor.rowcount,"Rows added successfully")
cursor.execute('commit')
'''

'''cursor.execute("alter table emp.emp_det rename column age to ages")
print(cursor.rowcount,"Row changed successfully")
cursor.execute('commit')'''

# cursor.execute('alter table emp.emp_det add salary decimal(5,2) ')
# cursor.execute('alter table emp.emp_det add location varchar(10) ')
# cursor.execute('alter table emp.emp_det add DOJ date')

'''cursor.execute('update emp.emp_det set location="Bengaluru" where location is NULL')
cursor.execute('commit')
print(cursor.rowcount,"row altered successfully")'''

'''val=[
    (100.12,101),
    (150.15,102),
    (107.10,103),
    (100.13,104),
    (100.11,105)
]

qur="update emp.emp_det set salary=%s where salary is Null and id=%s"

cursor.executemany(qur,val)
connect.commit()
'''
val = [
    ('2004-10-12', 101),
    ('2014-12-12', 102),
    ('2024-11-12', 103),
    ('2003-12-12', 104),
    ('1999-11-12', 105)
]

q = "UPDATE emp.emp_det SET doj = %s WHERE id = %s"

cursor.executemany(q, val)

connect.commit()

print(cursor.rowcount, "Rows updated successfully")



