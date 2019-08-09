n = input("Please enter 3 digit number only. hehe: ")
count = 0
d = {
    1:"one",
        
    2:"two",
        
    3:"three",
        
    4:"four",
        
    5:"five",
        
    6:"six",
        
    7:"seven",
        
    8:"eight",
        
    9:"nine"}

num = int(n)
num_str = ""
while num:
    count += 1
    digit = num % 10
    if count == 1:
        num_str = d[digit] + num_str
    if count == 2:
        if digit == 1:
            num_str = " ten " + num_str
        elif digit == 2:
            num_str = " twenty " + num_str
        elif digit == 3:
            num_str = " thirty " + num_str
        elif digit == 4:
            num_str = " forty " + num_str
        elif digit == 5:
            num_str = " fifty " + num_str
        else:
            num_str = d[digit] + "ty " + num_str
    if count == 3:
        num_str = d[digit] + " hundred " + num_str
    num = num // 10
print(num_str)

