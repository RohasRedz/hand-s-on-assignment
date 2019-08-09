def series(i):
    if i == 101:
        return
    print(i)
    i+=1
    series(i)

if __name__ == "__main__":
    i = 1
    series(i)
