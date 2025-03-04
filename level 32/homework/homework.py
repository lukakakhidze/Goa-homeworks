def sum_of_two_numbers(num1, num2):
    total = num1 + num2
    print("The sum of", num1, "and", num2, "is:", total)

sum_of_two_numbers(5, 3)


def reverse_string(s):
    reversed_s = s[::-1]
    return reversed_s

result = reverse_string("hello")
print("Reversed string:", result)


def find_maximum(numbers):
    return max(numbers)

numbers = [1, 5, 3, 9, 2]
result = find_maximum(numbers)
print("The maximum value is:", result)


def draw_square(size, char):
    for _ in range(size):
        print(char * size)

print("Red Square:")
draw_square(5, "#")
print("\nBlue Square:")
draw_square(5, "*")
print("\nGreen Square:")
draw_square(5, "&")
print("\nYellow Square:")
draw_square(5, "%")


