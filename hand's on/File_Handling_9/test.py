with open('ap.txt', 'r') as fd:
    lst = fd.readlines()
    s = "*".join(lst)
    print(s)
fd.close()