def func(*args):
    for i in args:
        print(i)

func(10,54,36,25,'asdf')


def func1(**kwargs):
    for i in kwargs.items():
        print(i)

func1(a=10,b=54,c=36,d=25,name='Mehedi')