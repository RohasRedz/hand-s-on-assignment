with open('test.txt', 'r') as fd:
    lst = fd.readlines()
    l = len(lst)
    for i in range(l-1, -1, -1):
        word_lst = lst[i].split()
        lw = len(word_lst)
        for j in range(lw-1, -1, -1):
            if "the" == word_lst[j]:
                word_lst[j] = word_lst[j].upper()
                lst[i] = " ".join(word_lst)

                break
        break

    st = "".join(lst)
    print(st)