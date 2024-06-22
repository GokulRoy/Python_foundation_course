import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="Gokul@1311",database="gokuldb")
mycursor = mydb.cursor()


# # for showing databases
# mycursor.execute("show databases")

# # for creating database
# mycursor.execute("create databases gokuldb")

# # for accessing database
# mycursor.execute("use gokuldb")


# # for creating tabale in the database
# mycursor.execute("crete table student(name varchar(50),college varchar(50))"

# # for showing tables
# mycursor.execute("show tables")

# # for inserting data into tables
# a = "insert into student (name,college)values(%s,%s)"
# val=("jhon","sret")
# mycursor.execute(a,val)
# # commit is very important then only it 
# # will update the data in table
# mydb.commit()


# # for print vallues which have college value sret
# a = "select * from student where college ='sret'"
# mycursor.execute(a)


# # for replace 
# a = "update student set college ='anna' where college ='sret'"
# mycursor.execute(a)
# mydb.commit()

# # for print vallues upto 5 rows
# a = "select * from student limit 5"
# mycursor.execute(a)


# # for delete the row in table
# a = "delete from student where name ='mike'"
# mycursor.execute(a)

# # for printing all data in tables
# mycursor.execute("select * from student")
# r = mycursor.fetchall()
# for i in r:
#     print(i)


# # to delete the table
# a = "drop student"
# mycursor.execute(a)



