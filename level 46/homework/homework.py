#2
my_tuple = (10, 20, 30, 40, 50)

second_element = my_tuple[1]
print("Second Element:", second_element)

last_element = my_tuple[-1]
print("Last Element:", last_element)

middle_slice = my_tuple[1:4]
print("Middle Slice:", middle_slice)


#3
my_tuple = (10, 20, 30, 40, 50)

try:
    my_tuple[1] = 100
except TypeError as e:
    print("Error:", e)


#4
my_tuple = (1, 2, 3, 4, 5)

a, b, c, d, e = my_tuple

print("Unpacked values:", a, b, c, d, e)


#5
my_tuple = (10, 20, 30, 20, 40, 20)

count_20 = my_tuple.count(20)
print("Count of 20:", count_20)

index_20 = my_tuple.index(20)
print("First occurrence of 20:", index_20)


#6
my_set = {1, 2, 3, 4, 5}

my_set.add(6)
print("Set after adding 6:", my_set)

my_set.remove(2)
print("Set after removing 2:", my_set)

is_3_present = 3 in my_set
print("Is 3 present in the set?", is_3_present)


#7
my_list = [1, 2, 2, 3, 4, 4, 5]

my_set = set(my_list)
print("Set after removing duplicates:", my_set)

unique_list = list(my_set)
print("List after removing duplicates:", unique_list)
