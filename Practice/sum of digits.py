num = int(input("Enter a number: "))
total = 0

while (num > 0):
    d = num % 10
    total = total + d
    num = num // 10
print("The sum of digits is: ", total)
