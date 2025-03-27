def max_number(numbers):
    return max(numbers)

def max_number_loop(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def sum_of_squares_of_positive(numbers):
    return sum(num**2 for num in numbers if num > 0)


numbers = [3, -5, 7, -2, 4, -1]

print("Max using max():", max_number(numbers))
print("Max using loop:", max_number_loop(numbers))

print("Sum of squares of positive numbers:", sum_of_squares_of_positive(numbers))
