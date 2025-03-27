def hello_world():
    print("Hello, World!")

hello_world()


def add_numbers(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")

add_numbers(5, 7)


def multiply_by_10(number):
    result = number * 10
    return result

result = multiply_by_10(5)
print(result)  # Output will be 50


def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")  
greet()       


def outer_function():
    print("This is the outer function.")
    
    def inner_function():
        print("This is the inner function.")
    
    inner_function()

outer_function()


def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

check_even_odd([1, 2, 3, 4, 5, 6])


def find_maximum(numbers):
    max_num = numbers[0]
    
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return max_num

result = find_maximum([3, 5, 7, 2, 8, 6])
print(f"The maximum number is: {result}")


def filter_positive_numbers(numbers):
    positive_numbers = []
    
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    
    return positive_numbers

result = filter_positive_numbers([-1, 2, 3, -4, 5, -6])
print(f"Positive numbers: {result}")


def sum_divisible_by_3(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 3 == 0:
            total_sum += num
    return total_sum

result = sum_divisible_by_3(1, 100)
print(f"The sum of numbers divisible by 3 is: {result}")
