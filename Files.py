my_file = open("Alyssa.txt", 'a')

my_file2 = open("ToDo.py", 'r\n')
# print(my_file.readlines())

# print("hello")
# print("world")

my_file.writelines(['im writing from python\n'])

my_file.close()

my_file = open("Alyssa.txt")

for line in my_file.readlines():
     print(line, end="")
