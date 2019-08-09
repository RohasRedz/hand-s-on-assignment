def age(n):
    day = int(n[:2])
    month = int(n[2:4])
    year = int(n[4:])
    print("Your age is {} years {} months and {} days".format((2019-year),(8-month),(4-day)))

if __name__ == "__main__":
    n = input("Please enter your DOB in ddmmyyyy format: ")
    age(n)
