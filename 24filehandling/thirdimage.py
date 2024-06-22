# to extarct image we use rb intead of r
a = open("D:\\Python foundation course\\24filehandling\\WIN_2024.jpg","rb")
# to print the image jpg format
print(a.read())
x1 = open("D:\\Python foundation course\\24filehandling\\Mypic.jpg","wb")
# we usew following for printing the image in other format
for i in a:
    x1.write(i)