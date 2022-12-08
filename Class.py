class Person:
    species = 'Homosapien'
    

    def hello(self):
        print('Hello World')

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hi(self):
        print('Hi, my name is ' + self.name)

class Student(Person):
    role = 'student'

Alyssa = Student('Alyssa',18)
print(Alyssa.species)
print(Alyssa.name)
print(Alyssa.age)
print(Alyssa.role)
Alyssa.hello()

Alyssa.hi()

Ayo = Student('Ayo', 16)
print(Ayo.species)
print(Ayo.name)
print(Ayo.age)
print(Ayo.role)
Ayo.hello()

class Teacher(Person):
    role = 'teacher'

    def hi(self):
        print('Hi, my name is Mx. ' + self.name)

forlenza = Teacher('Forlenza', 184)
print(forlenza.role)

forlenza.hi()


