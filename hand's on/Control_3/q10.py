n = int(input("Enter the number to be reversed: "))
np = n
temp = 0
digit = 0
while n:
    digit = n % 10
    n = n//10
    temp = temp*10 + digit
print("Reverse of {} is {}".format(np, temp))
