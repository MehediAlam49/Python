#python object

class person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
        
        
    def talk(self):
        print(f"Hi i am {self.name}")
        
    def gender_type(self):
        print(f"I am {self.gender} person")

    def vote(self):
        if self.age > 18:
            print('I am Eligible for Vote.')
        else:
            print('I am not Eligible for vote')
            
obj1 = person('Mehedi Alam', 'Male', 25)
obj2 = person('Saika Akter', 'Female', 20)

obj1.talk()
obj1.gender_type()
obj1.vote()

obj2.talk()
obj2.gender_type()
obj2.vote()