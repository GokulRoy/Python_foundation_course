a = int(input("a:"))
b = int(input("b:"))
try:
    print("resource opened here")
    # for zero division error
    print(a/b)
    # for invalid input value error
    k = int(input("k:"))
    print(k)
# in the place of Exception we can use individual error
except ValueError as e:
    print("its a invalid value error")
# in the place of Exception we can use individual error
except ZeroDivisionError as e:
    print("its zero division error")
# Exception is for all unknow errors
except Exception as e:
    print(" unknown error is occured and the error is",e)
finally:
    print("resource closed here")