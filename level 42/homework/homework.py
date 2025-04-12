#1
def sum_of_even(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    return even_sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("Sum of even numbers:", sum_of_even(numbers))


#codewars

#5
def count_sheeps(sheep):
    return sheep.count(True)

#6) Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

#7
def greet(name):
    return f"Hello, {name} how are you doing today?"
