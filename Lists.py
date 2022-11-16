my_list= [
    "malice",
    "4EVER",
    'sickandtired',
    'maple',
    'true relation'
]
print(my_list)

my_list.append('aptmnt')

print(my_list)

print(my_list[2])

print(my_list[-1])

my_list[0]='Get Gone'

del my_list[-1]

print(len(my_list))
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)


# #Tuple test
# my_tuple=(
#      'malice',
#     'shift reality',
#     '4EVER'
#  )
# print(my_tuple)

# #Tuple is immutable therefore it cannot change
# my_tuple.append['sickandtired']

# del my_tuple[2]

# my_tuple[2]='AXXAD'

second_list=[
    'scaramouche',
    'tartaglia',
    'alhaitham'
    'ayato',
    'itto',
    'dainsleif'
]
print(my_list + second_list)

print('/'.join(my_list + second_list))