while True:
    year = input ("Enter year: ")
    try:
        year = int(year)
    except:
        print("Please enter a year")
        continue
    if (year < 0):
        print("Please enter a positive number")
        continue
    break
if (int (year) % 4) == 0:
    if (int (year) % 100) == 0:
        if (int (year) % 400) == 0:
            print(year, " is a leap year")
        else:
            print(year, " is not a leap year")
    else:
        print(year, " is a leap year")
else:
    print(year, "is not a leap year")