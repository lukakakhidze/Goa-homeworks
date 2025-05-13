#1 
strings = ['apple', 'banana', 'cherry']
uppercase_strings = list(map(lambda x: x.upper(), strings))


#2
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))


#3
add_five = list(map(lambda x: x + 5, numbers))


#4 
celsius_temperatures = [0, 10, 20, 30, 40]
fahrenheit_temperatures = list(map(lambda x: (x * 9/5) + 32, celsius_temperatures))


#5
words = ['apple', 'banana', 'cherry']
first_characters = list(map(lambda x: x[0], words))


#7
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers_filtered = list(filter(lambda x: x % 2 != 0, numbers))


#8
words = ['apple', 'banana', 'cherry', 'kiwi', 'grape']
long_words = list(filter(lambda x: len(x) > 5, words))


#9 
numbers_with_negatives = [-1, 2, -3, 4, -5, 6]
positive_numbers = list(filter(lambda x: x >= 0, numbers_with_negatives))


#10 
names = ['Alice', 'Bob', 'Anna', 'Charlie', 'Alex']
names_starting_with_A = list(filter(lambda x: x.startswith('A'), names))


#11 
numbers_for_division = [1, 2, 3, 4, 5, 6, 7, 8, 9]
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers_for_division))
