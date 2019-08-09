n1 = int(input("Enter 1st num: "))
n2 = int(input("Enter 2nd num: "))
l1 = []
l2 = []
for i in range(1,n1+1):
    if n1 % i == 0:
        l1.append(i)
for i in range(1,n2+1):
    if n2 % i == 0:
        l2.append(i)
gcd = 0
for i in l1:
    if i in l2:
        gcd = i
print("GCD is: {}".format(gcd))

lcm = 2
test = 1

while True:
    if lcm % n1 == 0 and lcm % n2 == 0:
        print("LCM is: {}".format(lcm))
        break
    else:
        lcm += 1
    
