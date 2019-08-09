a = int(input("Enter first number: "))

b = int(input("Enter second number: "))


def swap(a,b):

    a = a+b

    b = a-b

    a = a-b

    return a,b

print("Numbers are ", a, " and ", b)    

print("numbers swapped: ", swap(a,b) )