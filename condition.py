# if statement
a = 30

if a>=18:
    print('You are voter')
    
    
# if-else statement
x = 25
if x%2==0:
    print('x is a even number')
else:
    print('x is odd number')
    
#nested if statement
z = 33
if z>25:
    if z%2 == 0:
        print('Number is grater then 25 and even number')
    else:
        print('Number is grater then 25 and odd number')
else:
    print('Number is less then 25')
    
    
    
# if-elif-else statement
l = 'o'
if l == 'a':
    print('This is a vowel and letter is a')
elif l == 'e':
    print('This is a vowel and letter is e')
elif l == 'i':
    print('This is a vowel and letter is i')
elif l == 'o':
    print('This is a vowel and letter is o')
elif l == 'u':
    print('This is a vowel and letter is u')
else:
    print('This is a Consonent')
    
    
# turnery operator
score = 25
status = 'pass' if score >= 40 else 'Fail'
print(status)
    