frstName = "chenchu gokul"
lastName = "jangam"
s = frstName + " " + lastName
# python provide numeros methods to manupulate such as
# conveting case
print(s.upper())
print(s.lower())
# for making first letter r starting letter capital
print(s.capitalize())
#removing white spaces
print(s.strip())
print(s.rstrip())
print(s.lstrip())
# converting the first alphabet of each word to uppercase and the rest into lowe
print(s.title())
#replaceing str index
print(s.replace('k','c'))
# to count the repeated letters
print(s.count('a'))
print("abracadbra".count('a'))
# checks weather the string starts with the given letter or not
print(s.startswith("c"))
print(s.startswith("a"))
# checks weather the string ends with the given letter or not
print(s.endswith("m"))
print(s.endswith("a"))
# we split the string into a list of two elements
print(s.split())
# joins first and last by seperating given str or adding str btwn the given str
print(s.join("012"))

