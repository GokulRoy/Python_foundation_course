# converting Temperature Units
# i: temp_celsius=30
# o: temp in fahrenheit=86.0; temp in kelvin=303.15
C = int(input("Temp in celsius = "))
F = (C * (9 / 5) + 32)
K = 273 + C
print(f"Temp in fahrenheit: {F}, Temp in kelvin: {K}")