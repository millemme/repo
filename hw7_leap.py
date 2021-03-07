def leap_year(x):
    if (x % 4 == 0):
        if (x % 100 == 0):
            if (x % 400 == 0):
                return "yes"
            else:
                return "no"
        else:
            return "yes"
    else:
        return "no"

def main():  
    x = input ("Enter year: ")
    print(leap_year(x))

if __name__ == '__main__':
    main()