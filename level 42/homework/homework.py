def sum_of_even(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    return even_sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("Sum of even numbers:", sum_of_even(numbers))


#codewars