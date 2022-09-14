color1 = input("Enter color 1:")
color2 = input("Enter color 2:")

if color1 == ("red") and color2 == ("blue"):
    print("Purple")
elif color1 == ("blue") and color2 == ("red"):
    print("Purple")
elif color1 == ("red") and color2 == ("yellow"):
    print("Orange")
elif color1 == ("yellow") and color2 == ("red"):
    print("Orange")
elif color1 == ("yellow") and color2 == ("blue"):
    print("Green")
elif color1 == ("blue") and color2 == ("yellow"):
    print("Green")
else:
    print("Error")
