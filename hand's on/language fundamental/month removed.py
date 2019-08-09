month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
 'August', 'September', 'October', 'November', 'December']
              

n = int(input("Enter your birthday month number: "))
	          


if n > 0  and n<13 :

    for i in range(0,len(month_lst)):

        if i+1 == n:

            month_lst.pop(i)

            print("removed")

        else:
 
            continue


print("Month: ", month_lst)
        
    