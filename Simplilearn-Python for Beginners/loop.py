
# while loop
num = int(input("Enter a number that is a multiple of 7: "))
while num % 7 != 0:
    print(f"{num} is not a multiple of 7.")
    num = int(input("Try again: "))
print(f"{num} is a multiple of 7!")

# for loop
z = [3,8,'mehedi','saiful']
for i in z:
    print(i)
    
# nested loop 
x = [[1,3,56],['a','b','c']]
for i in x:
    for j in i:
        print(j, end='')
    print()
