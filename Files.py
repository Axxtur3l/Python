my_file = open("Alyssa.txt", 'r+')

# print(my_file.readlines())

for line in my_file.readlines():
     print(line, end="")

my_file.writelines(['im writing from python'])

# print("hello")
# print("world")