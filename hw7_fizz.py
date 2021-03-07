def fizz_buzz(x):
    if (x % 3 == 0):
        return "Fizz"
    else:
        return x


def main():
    x = 1;
    while x < 101:
        print(fizz_buzz(x))
        x = x + 1
