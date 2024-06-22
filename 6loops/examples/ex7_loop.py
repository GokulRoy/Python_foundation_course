# multiplication of tables from 1 to n using while
n = int(input("N="))
print(f"Multiplication table of {n}")
i = 1
while i<=10:
    print(f"{n}x{i}={i*n}")
    i+=1
    