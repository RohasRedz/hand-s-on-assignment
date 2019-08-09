def sumOfDigits(n):
    s = 0
    d = 0
    while n:
        d = n % 10
        s += d
        n = n // 10
    return s

if __name__ == "__main__":
    n = int(input())
    print("The sum of digits of {} is {}".format(n, sumOfDigits(n)))
