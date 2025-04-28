#f1
squares = [x**2 for x in range(1, 11)]
print(squares)

#2
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)

#3
words = ["apple", "banana", "cherry", "date"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

#4
word_lengths = [len(word) for word in words]
print(word_lengths)

#5
numbers = [1, 2, 3, 4, 5]
numbers_plus_5 = [num + 5 for num in numbers]
print(numbers_plus_5)

#6
first_letters = [s[0] for s in words]
print(first_letters)

#7
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)
