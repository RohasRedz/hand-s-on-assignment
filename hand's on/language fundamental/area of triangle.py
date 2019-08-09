h = int(input("Enter the height of triangle:"))

b = int(input("Enter the base of triangle:"))


def area(a,b):

    if (a>0 and b>0):

        ar = a*b/3

        return ar


print(area(h,b))
