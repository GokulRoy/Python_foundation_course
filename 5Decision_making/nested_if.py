w = input()
day_or_night = input()

if w == "sunny":  # colun(:) verey important
    if day_or_night == "day":
        print("you can play outside")   #space or indentation is also important
    else:
        print("you need to sleep")
elif w == "rainny":
    print("play indore games")
elif w == "snow" and day_or_night == "night":
    if day_or_night == "night":
        print("you can play inside with teddy")   #space or indentation is also important
    else:
        print("you can play outside with snowman")
else:
    print("you can play inside")
print("have fun!")