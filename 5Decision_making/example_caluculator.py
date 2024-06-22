num1 = int(input("give num1 value = "))
num2 = int(input("give num2 value = "))
operator = input("give operator : ")
if operator == "+": 
    print(f"sum of 2 numbers {num1+num2}")  
elif operator == "-":
    print(f"sub of 2 numbers {num1-num2}") 
elif operator == "*":
    print(f"mul of 2 numbers {num1*num2}")
elif operator == "/":
    print(f"div of 2 numbers {num1/num2}")
else:
    print("enter valid operator i.e.. +, -, *, /")