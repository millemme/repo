def cube(x):
    if type(x) is not int:
        return True
    else :
        return x * x * x

def avg(list):
    if len(list) == 0:
        raise Exception("Empty String")
    return sum(list) / len(list)

def combine(first, last):
    space = " ";
    return first + space + last