def leap_year(x):
    if (x % 4 == 0):
        return "yes"
    return "no"

def main():  
    x = input ("Enter year: ")
    print(leap_year(x))

if __name__ == '__main__':
    main()