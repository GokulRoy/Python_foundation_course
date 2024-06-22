a = int(input("a:"))
b = int(input("b:"))
# now here we use try to identify the error
try:
    print(a/b)
# now if error identified the below must be done
except Exception:
    print("you have givrn b as zero")

print("bye")