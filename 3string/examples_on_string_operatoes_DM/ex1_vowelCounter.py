# program to take a string input from the user and
# count the number of vowles (a,e,i,o,u) and their lower case equvalent
s = input("Enter the string:")
s = s.lower()
a = s.count('a')
e = s.count('e')
i = s.count('i')
o = s.count('o')
u = s.count('u')
print(f"Number of vowels:{a+e+i+o+u}")
