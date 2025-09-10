
def compute_gdc(x,y):
  if x > y:
    smaller = y
  else:
    smaller = x
  for i in range(1, smaller + 1):
    if((x % i == 0) and (y % i == 0)):
      gdc = i
  return gdc
num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
print("The GDC of", num1, "and", num2, "is: ", compute_gdc(num1, num2))
