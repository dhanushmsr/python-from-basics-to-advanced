import pymysql 

# pymysql.connect() {paramters{user,password,host,database}} 

con_obj=pymysql.connect(user='root',password='root',host='localhost')#database='adv'

cur_obj=con_obj.cursor()

#connect object is used bridge connections between python software and mysql software using pymysql module
#cursor object is used to implement or work with database ie., tables.
#cursor object will have a group i.e., objects of databases
cur_obj.execute('show databases')
for i in cur_obj:
    print(i)

# cur_obj.execute('create database adv') 
# #only one time to create it or else it will raise error (drop the database using drop database <database name>)
# print('database create')

# cur_obj.execute('create table adv.stu_det(id varchar(10),name varchar(20),age int(2))')
# print('table create')
# cur_obj.execute("insert into adv.stu_det(id,name,age) value('123dm','dhanush','21')")
# print("values are inserted")
# cur_obj.execute('commit') #or con_obj.commit()

#insert multiple values at the time
'''
qru="insert into adv.stu_det(id,name,age) values(%s,%s,%s)"
values=[
    ('124dm','thanuder',22),
    ('125dm', 'wonder',23),
    ('126dm','land',21)
]

cur_obj.executemany(qru,values)
con_obj.commit()
'''

#to count the number of rows
print(cur_obj.rowcount ,"number of rows presented")


#update the value in the table
cur_obj.execute('update adv.stu_det set age=25 where age<22')
con_obj.commit()

#delete the value in the table
cur_obj.execute('delete from adv.stu_det where id="125dm"')
con_obj.commit()

print(cur_obj.rowcount ,"number of rows deleted")

# cur_obj.execute('alter table adv.stu_det add salary int(5)')
# print(cur_obj.rowcount ,"created")

# cur_obj.execute('alter table adv.stu_det add location varchar(10)')
# cur_obj.execute('alter table adv.stu_det add doj date')
con_obj.commit()

cur_obj.execute('update adv.stu_det set location="btm" where location is Null')
print("value is added")
con_obj.commit()


