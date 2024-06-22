# during loop we encounter break value there the loop will cancle
c = 10
for i in range (c):
    # give one candy to a friend
    print("give candy")
    print(i)
    # checks if there are only 5 candies
    if c - i == 5:
        print("only 5 candies left")
        # here we break the loop stops
        break
print(f"remaining candies:{i}")
