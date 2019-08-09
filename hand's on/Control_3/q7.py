print("Primes between 25 and 75 are: ")
flag = 0
for i in range(25, 75):
    flag = 0
    rt = int(i ** 0.5)
    for j in range(2, rt+1):
        if i % j == 0:
            flag = 1
    if flag == 0:
        print(i)
    
            
            
