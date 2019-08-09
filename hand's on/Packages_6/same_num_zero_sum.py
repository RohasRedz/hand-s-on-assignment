lst = []
while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    else:
        lst.append(n)
su = 0
l = len(lst)
for i in range(l):
    if lst[i] in lst[i+1:]:
        su = 0
        break
    else:
        su += lst[i]

print(su)