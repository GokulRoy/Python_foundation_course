w = input()
day_or_night = input()
if w == "sunny":  # colun(:) verey important
    print("you can play outside")   #space or indentation is also important
elif w == "rainny":
    print("play indore games")
elif w == "snow" and day_or_night == "night":
    print("play indore games")
else:
    print("you can play inside")

print("have fun!")