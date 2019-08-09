def max_word_length(lst):
    mx = 0
    idx = 0
    l = len(lst)
    for i in range(l):
        if len(lst[i]) > mx:
            mx = len(lst[i])
            idx = i
    return mx,idx

lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
mx, idx = max_word_length(lst)
print("The longest month name is {} with length {}".format(lst[idx], mx))
