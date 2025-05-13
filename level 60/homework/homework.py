#1
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = num1 / num2
        print(f"The result of division is: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numeric values.")

divide_numbers()


#2
def convert_to_integer():
    user_input = input("Enter a string to convert to an integer: ")
    
    try:
        number = int(user_input)
        print(f"Conversion successful! The integer is: {number}")
    except ValueError:
        print("Error: The input is not a valid integer.")

convert_to_integer()


#3
def access_list_element():
    my_list = ['apple', 'banana', 'cherry', 'date', 'fig']

    print(f"My list: {my_list}")
    user_input = input("Enter an index to access an element: ")

    try:
        index = int(user_input)
        print(f"Element at index {index}: {my_list[index]}")
    except ValueError:
        print("Error: Please enter a valid integer index.")
    except IndexError:
        print("Error: Index is out of range. Try a number between 0 and", len(my_list) - 1)

access_list_element()


#4
def add_two_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        result = num1 + num2
        print(f"The sum is: {result}")
    except ValueError:
        print("Error: Please enter valid integers.")

add_two_numbers()


#5
def safe_list_removal():
    fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
    print(f"Current list: {fruits}")

    item_to_remove = input("Enter the item you want to remove: ")

    try:
        fruits.remove(item_to_remove)
        print(f"'{item_to_remove}' has been removed.")
        print(f"Updated list: {fruits}")
    except ValueError:
        print(f"Error: '{item_to_remove}' is not in the list.")

safe_list_removal()
