class Person:
    species = 'Homosapien'
    

    def hello(self):
        print('Hello World')

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hi(self):
        print('Hi, my name is ' + self.name)

Alyssa = Person('Alyssa',18)
print(Alyssa.species)
print(Alyssa.name)
print(Alyssa.age)
Alyssa.hello()

Alyssa.hi()

Ayo = Person('Ayo', 16)
print(Ayo.species)
print(Ayo.name)
print(Ayo.age)
Ayo.hello()