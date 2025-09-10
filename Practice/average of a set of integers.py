num = int(input("Enter a number(To be average first to current number): "))
total_num = num
print("The current Number is: ", total_num)
sum = 0
while(num>0):
    sum += num
    num -= 1
print("The sum of numbers is: ", sum)
average = sum / total_num
print("The Average Number is: ", average)
