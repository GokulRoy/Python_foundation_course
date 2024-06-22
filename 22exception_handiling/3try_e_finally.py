a = int(input("a:"))
b = int(input("b:"))

# use try to find error amd here the resoure is opened
try:
    print("resource opened here")
    # if error find here the error will be here and prints this error
    # if not the below
    print(a/b)
    # if error find here prints this error
    k = int(input("k:"))
    print(k)
# Exception is for all unknow errors
# in the place of Exception we can use individual error
except Exception as e:
    print("error is occured and the error is",e)
# now to close we use 'finally' 
# then here the resource will be closed
# either error occured or not
finally:
    print("resource closed here")