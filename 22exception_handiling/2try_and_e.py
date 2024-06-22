a = int(input("a:"))
b = int(input("b:"))

# use try to find error
try:
    print(a/b)
# now use 'e' in except to konw the error
# here is the type of error
except Exception as e:
    print("error is occured and the error is",e)