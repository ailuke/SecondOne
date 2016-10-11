askyear = input("Give me a year! ")

if int(askyear) % 4 == 0:
    print("This is a leap year")
    if int(askyear) % 100 == 0 and int(askyear) % 400 == 0:
        print("This is a leap year")
else:
    print("This is not a leap year")
