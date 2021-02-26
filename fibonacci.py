def fibs(x)
    count = 0
    num1 = 0
    num2 = 1
    curr = 0
    fib_list = []
    if (x == 1):
        return 0
    else:
        fib_list.append(0)
        while (count < x):
            print(num1)
            curr = num1 + num2
            num1 = num2
            num2 = curr
            count += 1
            fib_list.append(curr)
        return fib_list
def factorial(x)
    fact = 1
    if (x == 0):
        return 1
    else:
        for i in range(1, x + 1):
            fact = fact*i
        return fact