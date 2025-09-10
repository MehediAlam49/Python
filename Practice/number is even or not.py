num = int(input("Enter a Number to check Even or Not: "))
if(num >= 0):
    if(num % 2 != 0):
        print(num, "is not Even Number.")
    else:
        print(num, " is Even Number.")
else:
    print(num, "is Negetive Number, please Enter a positive Number.")
