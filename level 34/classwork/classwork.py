def calculator(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operator!")

calculator(5, 3, "+")  # 5 + 3
calculator(10, 4, "-")  # 10 - 4
calculator(6, 2, "*")   # 6 * 2


def find_minimum(user_list):
    min_value = user_list[0] 
    for num in user_list:
        if num < min_value:
            min_value = num 
    print(min_value)

find_minimum([5, 2, 9, 1, 7])  # 1
find_minimum([10, 15, 3, 8, 12])  # 3
find_minimum([20, 100, 50, 10])  # 10
find_minimum([11, 9, 5, 8, 2])   # 2
find_minimum([7, 4, 6, 3])       # 3


def manual_capitalize(user_str):
    return user_str[0].upper() + user_str[1:].lower()

user_input = input("გთხოვთ შეიტანოთ ტექსტი: ")

result = manual_capitalize(user_input)
print("Capitalized ტექსტი:", result)
