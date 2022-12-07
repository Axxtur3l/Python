try:
    age = int(input('Enter your age: '))
    faveNum = int(input('What is your favorite number: '))

    if age <= 21:
       print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
    
    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except ValueError or TypeError: 
    print(int(input("Dawg...use a real number: ")))
except ZeroDivisionError:
    print(int(input("Ew, Imagine liking 0, put in a real number you fool: ")))
finally:
    print("Joe")
# except:
#     print (int(input("Input a number you bozo: ")))
