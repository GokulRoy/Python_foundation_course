# to create the file we use directory and file name
# and use "w" to write
f1 = open("D:\\Python foundation course\\24filehandling\\secondtext","w")
# "write" is used to add data
print(f1.write("laptop"))
f2 = open("D:\\Python foundation course\\24filehandling\\secondtext","a")
# and use "a" to append
print(f2.write(" mobile"))