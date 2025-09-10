print("find H.C.F or GCD of two numbers in python are given below: ")

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input("Enter 1st Number: ")) 
num2 = int(input("Enter 2nd Number: ")) 

print("The H.C.F. is: ", compute_hcf(num1, num2))
