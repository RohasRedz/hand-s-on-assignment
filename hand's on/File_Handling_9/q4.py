fd = open('test.txt', 'r')
lst = fd.readlines()
count = 0
for line in lst:
    if "test" in line:
        count += 1
print(count)