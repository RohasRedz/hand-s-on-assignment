def splitWord(word, numOfChar):
    l = len(word)
    new_lst = []
    while word:
        i = 0
        i += numOfChar
        new_lst.append(word[:i])
        word = word[i:]
    return new_lst

if __name__ == "__main__":
    print(splitWord("bingbangbongbung",4))
    
