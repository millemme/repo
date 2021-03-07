def leap_year(x):
    if (x % 100 == 0):
        return "no"
    elif (x % 4 == 0):
        return "yes"
    else:
        return "no"

def main():  
    x = input ("Enter year: ")
    print(leap_year(x))

if __name__ == '__main__':
    main()