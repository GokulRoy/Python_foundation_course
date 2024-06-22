# multiplication of tables from 1 to n using for
n = int(input("N="))
print(f"Multiplication tables of 1to{n}")
for i in range(1,n+1):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")


# multiplication table of Y th number
y = int(input("Y="))
print(f"Multiplication table of {y}")
for a in range(1,11):
    print(f"{y}x{a}={y*a}")

