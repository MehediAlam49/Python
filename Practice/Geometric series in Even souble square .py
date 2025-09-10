n = int(input("Enter the last Number: "))
mul = 1
for x in range(2, n + 1, 2):
    mul = mul * (x * x)
print(mul)
