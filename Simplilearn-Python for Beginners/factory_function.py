# Factory Function
print('Factory Function:')
def animal_factory(kind):
    if kind == 'dog':
        return('Woof!')
    elif kind == 'cat':
        return('meow!')
    else:
        return('unknown animal')
    
print(animal_factory('dog'))
print(animal_factory('cat'))




# Factory function with class
print('\nFactory function with class:')
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_factory(kind):
    if kind == "dog":
        return Dog()
    elif kind == "cat":
        return Cat()
    else:
        raise ValueError("Unknown animal")

animal = animal_factory("dog")
print(animal.speak()) 




# Factory function with closure
print('\nFactory function with closure:')

def multiplier_factory(n):
    def multiplier(x):
        return x * n
    return multiplier

double = multiplier_factory(2)
triple = multiplier_factory(3)
print(double(5))
print(triple(5))


# Decorator as a Factory
print('\nDecorator as a Factory:')
def greet_factory(prefix):
    def decorator(func):
        def wrapper(name):
            print(f"{prefix}, {name}")
            func(name)
        return wrapper
    return decorator

@greet_factory('Hello')
def my_func(name):
    print('Welcome to python.')

@greet_factory('Hi')
def my_other_func(name):
    print('Have a greet day.')
    
my_func('Mehedi')
my_other_func('Alam')