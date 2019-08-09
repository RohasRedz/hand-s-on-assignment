import sys
x = int(sys.argv[1])
sq_x = x ** 2
rt_x = x ** 0.5
print(sq_x)
print(rt_x)
count = 0
d = {
    1: "one",

    2: "two",

    3: "three",

    4: "four",

    5: "five",

    6: "six",

    7: "seven",

    8: "eight",

    9: "nine"}

num_str = ""
while x:
    count += 1
    digit = x % 10
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
        num_str = d[digit] + " hundred" + num_str
    x = x // 10
print(num_str)