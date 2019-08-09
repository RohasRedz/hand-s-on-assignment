import sys
lst = []
for i in range(1, len(sys.argv)):
    lst.append(sys.argv[i])

lst.sort(key=len)
print(lst)