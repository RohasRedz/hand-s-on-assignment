import sys
sum = 0
for i in sys.argv:
    try:
        if isinstance(int(i), int):
            sum += int(i)
    except ValueError:
        continue
    except TypeError:
        continue
print(sys.argv)
print(sum)