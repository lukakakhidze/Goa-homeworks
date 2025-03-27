number = int(input("Please enter an integer: "))

if number > 0:
    print("Bigger than 0")
elif number == 0:
    print("0")
else:
    print("Smaller than 0")


first_number = int(input("Please enter the first integer: "))
second_number = int(input("Please enter the second integer: "))

if first_number > second_number:
    for i in range(second_number, first_number + 1):
        print(i)
elif second_number > first_number:
    for i in range(first_number, second_number + 1):
        print(i)
else:
    print("Numbers are equal")


score = int(input("Enter the score (0-100): "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
else:
    print("Grade: F")


#elif რომელიც გამოიყენება ერთზე მეტი პირობის დასაყენებლად. ეს საშუალებას გვაძლევს, გავაკეთოთ დამატებითი პირობები, რომლებიც უნდა შემოწმდეს, თუ ძირითადი if პირობა არ შესრულდა.

                #როდის ვიყენებთ elif?

#elif გამოიყენება, როდესაც გვაქვს რამდენიმე პირობა, რომლითაც უნდა შევამოწმოთ მნიშვნელობა. მაგალითად, თუ პირველი პირობა არ შესრულდა, elif დაგვეხმარება მეორე პირობის შესამოწმებლად და ასე შემდეგ.


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")


correct_password = "Goa best"
incorrect_attempts = 0

while True:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Password correct!")
        break  
    else:
        incorrect_attempts += 1  
        print(f"Incorrect password. You have attempted {incorrect_attempts} times.")

print(f"Total incorrect password attempts: {incorrect_attempts}")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator! Please enter +, -, *, or /."

print(f"The result is: {result}")