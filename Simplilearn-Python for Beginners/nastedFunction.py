#Nested function
def func():
    x = 10
    def func2(x):
        return x+1
    return func2(x)

result = func()
print(result)