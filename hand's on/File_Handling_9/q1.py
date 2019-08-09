try:
    fd = open('file.py', 'r')
except FileNotFoundError:
    print("File does not exist")
else:
    print("File exists")