try:
    x = int(input())
    y = int(input())
    res = x/y

except ZeroDivisionError:
    print("Can't divide by Zero:")

else:
    print(res)

finally:
    print("Error or no error mai print hoga na.")