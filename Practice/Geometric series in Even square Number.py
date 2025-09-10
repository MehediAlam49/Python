n = int(input("Enter the last Number: "))
mul = 1
for x in range(1, n + 1, 1):
    mul = mul * (x * x)
print(mul)
