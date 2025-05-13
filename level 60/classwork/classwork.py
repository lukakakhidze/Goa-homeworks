#1
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = num1 / num2
        print(f"The result of division is: {result}")
    
    except ValueError:
        print("Error: Please enter valid numeric values.")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

divide_numbers()


#2
try:
    number = int(input("შეიყვანეთ რიცხვი: "))
    print(f"შეიყვანეთ რიცხვი: {number}")
except ValueError:
    print("გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")
