nums = [0,1,2,3,4,5,6,7,8,9,0]
s = int(input("Enter the number to be searched: "))
count = 0
for i in nums:
    if s == i:
        count += 1
print("{} is present {} times".format(s,count))
