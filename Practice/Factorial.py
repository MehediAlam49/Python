n = int(input("Enter a Number for Factorial: "))
fac = 1
for x in range(1, n + 1):
    fac = fac * x
print("The factorial Number of" , x , "is: " , fac)
