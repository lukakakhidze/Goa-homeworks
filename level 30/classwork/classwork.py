my_list = [
    "Hello",      # string
    3.14,         # float
    42,           # integer
    True,         # boolean
    False,        # boolean
    ["apple", "banana"],  # list
    ["car", "bike"],      # list
    7.89,         # float
    "World",      # string
    100           # integer
]


my_list = [
    "apple",    # string
    3.14,       # float
    42,         # integer
    True,       # boolean
    False,      # boolean
    ["cat", "dog"],  # list
    ["red", "green", "blue"],  # list
    100,        # integer
    7.89,       # float
    "banana",   # string
    "grape",    # string
    200,        # integer
    0.56,       # float
    "melon",    # string
    True        # boolean
]

reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)


# 10 ელემენტიანი სია
my_list = [
    "apple",    # string
    3.14,       # float
    42,         # integer
    True,       # boolean
    False,      # boolean
    ["cat", "dog"],  # list
    ["red", "green", "blue"],  # list
    100,        # integer
    7.89,       # float
    "banana"    # string
]
sliced_1 = my_list[-3:]
print("Sliced 1:", sliced_1)

sliced_2 = my_list[-5:]
print("Sliced 2:", sliced_2)

sliced_3 = my_list[-7:-2]
print("Sliced 3:", sliced_3)

sliced_4 = my_list[-1:-10:-2]
print("Sliced 4:", sliced_4)

sliced_5 = my_list[::-1]
print("Sliced 5:", sliced_5)