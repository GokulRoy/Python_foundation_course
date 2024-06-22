c = 10
for i in range (c):
    print(i)

    # checks if there is only 5 candies
    if c - i == 5:
        print("only 5 candies left,skip this turn")
        # here we break the loop stops
        continue
    print(i)
print(f"remaining candies:{i}")