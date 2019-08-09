a = int(input("Enter number: "))



def divisible(a):

    if a!=0:

        if a%5==0:

            return "Divisible by 5"

        else:

            return  "Not divisible by 5"




print("numbers swapped: ", divisible(a) )