lst = []
while True:
    n = int(input("Enter a number: "))
    if n == 0:
        print("Inputs will be terminated. Zero has been entered: ")
        break
    lst.append(n)
sump = 0
sumn = 0
mn = 0
mx = 0
count = 0
for i in lst:
    if i < mn:
        mn = i
    if i > mx:
        mx = i
    if i < 0:
        sumn += i
    if i > 0:
        sump += i
    count += 1
print("Sum of all positive numbers: {} ".format(sump))
print("Sum of all negative numbers: {} ".format(sumn))
print("Max {} ".format(mx))
print("Min: {} ".format(mn))
print("Length: {}".format(count))
