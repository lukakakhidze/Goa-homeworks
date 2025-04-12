#1
print("Luka kakhidze")


#2
print('"The only limit to our realization of tomorrow is our doubts of today." - Franklin D. Roosevelt')


#3
print("Roses are red,")
print("Violets are blue,")
print("Python is fun, and so are you!")


#4
print(2 + 3)


#5
print("#####")
print("#   #")
print("#   #")
print("#   #")
print("#####")


#6
numeric_string = "42"
converted_integer = int(numeric_string)
print(converted_integer)


#7
float1 = 3.5
float2 = 2.5
sum_of_floats = float1 + float2
print(sum_of_floats)


#8
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print(concatenated_string)


#9
integer_variable = 5
string_variable = "Python"
float_variable = 3.14

print(type(integer_variable))
print(type(string_variable))
print(type(float_variable))


#10
age = input("11 ")
age_next_year = int(age) + 1
print("12", age_next_year)


#11
name = input("What is your name? ")
print(f"Hello, {name}!")


#12
age = int(input("How old are you? "))
next_year_age = age + 1
print(f"Next year, you will be {next_year_age} years old.")
age = int(input("How old are you? "))
next_year_age = age + 1
print(f"Next year, you will be {next_year_age} years old.")


#13
num1 = int(input(" 7 "))
num2 = int(input(" 17"))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")


#14
favorite_color = input("What is your favorite color? ")
print(f"Your favorite color is {favorite_color}!")


#15
height = int(input("140"))
if height > 150:
    print("You are tall enough!")
else:
    print("Sorry, you are not tall enough.")


#16
for i in range(1, 6):
    print(i)


#17
word = "Python"
for letter in word:
    print(letter)


#18
total = 0
for i in range(1, 11):
    total += i
print("Sum is:", total)


#19
for i in range(1, 6):
    print(f"2 x {i} = {2 * i}")


#20
for i in range(2, 21, 2):
    print(i)


#21
i = 1
while i <= 5:
    print(i)
    i += 1


#22
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Sum is:", total)


#23
i = 10
while i >= 1:
    print(i)
    i -= 1


#24
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1


#25
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter something (type 'exit' to quit): ")
print("Exited successfully!")


#26
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


#27
my_list = [1, 2, 3, 4, 5]
print("Number of elements:", len(my_list))


#28
numbers = [10, 20, 30, 40]
print("Second element:", numbers[1])  # Index 1 არის მეორე ელემენტი


#29
animals = ["cat", "dog", "rabbit"]
animals.append("hamster")
print("Updated list:", animals)


#30
colors = ["red", "green", "blue"]
colors.remove("green")
print("After removal:", colors)


#31
squares = [x**2 for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]


#32
evens = [x for x in range(2, 11) if x % 2 == 0]
print(evens)
# Output: [2, 4, 6, 8, 10]


#33
numbers = [1, 2, 3, 4, 5, 6, 7]
odds = [x for x in numbers if x % 2 != 0]
print(odds)
# Output: [1, 3, 5, 7]


#34
words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)
# Output: ['APPLE', 'BANANA', 'CHERRY']


#35
nums = [1, 2, 3, 4, 5, 6]
squared_evens = [x**2 for x in nums if x % 2 == 0]
print(squared_evens)
# Output: [4, 16, 36]


#36
def greet_user(luka):
    print(f"Hello, {luka}!")


#37
def add_numbers(a, b):
    return a + b


#38
def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


#39
def rectangle_area(length, width):
    return length * width


#40
def reverse_string(s):
    return s[::-1]


#41
my_tuple = (10, "hello", 3.14)
print(my_tuple)


#42
items = ("apple", "banana", "cherry", "date")
print("Second element:", items[1])  # Index 1 = banana


#43
numbers = (1, 2, 3, 4, 5)
print("Length of tuple:", len(numbers))


#44
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
combined = tuple1 + tuple2
print("Combined tuple:", combined)


#45
colors = ("red", "green", "blue")
if "green" in colors:
    print("Found")
else:
    print("Not found")


#46
my_set = {1, "hello", 3.14}
print(my_set)


#47
fruits = {"apple", "banana", "cherry"}
if "banana" in fruits:
    print("Yes")
else:
    print("No")


#48
colors = {"red", "green"}
colors.add("blue")
print("Updated set:", colors)


#49
numbers = {1, 2, 3, 4}
numbers.remove(3)
print("After removal:", numbers)


#50
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Union:", union_set)


#51
person = {
    "name": "Luka",
    "age": 11
}
print(person)


#52
person = {
    "name": "Luka",
    "age": 25
}
print("Name:", person["name"])


#53
person = {
    "name": "Luka",
    "age": 25
}
person["city"] = "Tbilisi"
print("Updated dictionary:", person)

