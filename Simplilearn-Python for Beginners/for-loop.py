x = [3,8,'Mehedi']
for i in x:
    print(i)
    
# range method for print 0-20
for i in range(0,21):
    print(i)
    
    
# range method for print 0-20 in after a number
for i in range(0,21,2):
    print(i)
    
    
# sum of number using range
total = 0
for i in range(0, 21, 2):
    total += i
print(f"The total sum of even numbers from 0 to 20 is {total}")