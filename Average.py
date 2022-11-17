x = input('Enter your grades with commas: ')

grades = x.split(',')

sum = 0
for grade in grades:
    sum = sum + int(grade)

print(sum / len(grades))