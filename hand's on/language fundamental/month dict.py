month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
 'August', 'September', 'October', 'November', 'December']
              

print(month_lst.keys())

monthies = list(month_lst.keys())


month = input(" Enter the month from above list: ")


if month in monthies:

    print("Days: ", month_lst[month])

else:

    print("Invalid Input")