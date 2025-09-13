num = int(input("Enter a number that is a multiple of 7: "))
while num % 7 != 0:
    print(f"{num} is not a multiple of 7.")
    num = int(input("Try again: "))
print(f"{num} is a multiple of 7!")