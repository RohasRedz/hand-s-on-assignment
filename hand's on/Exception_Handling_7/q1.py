print("Enter 5 numbers: ")
lst = []
count = 0
try:
    while count < 5:
        count += 1
        lst.append(int(input("-> ")))
except ValueError:
    print("Please enter only integers")