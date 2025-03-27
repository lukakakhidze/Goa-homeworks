number = int(input("შეიყვანეთ მთელი რიცხვი: "))

if number > 0:
    print("Bigger than 0")
elif number == 0:
    print("0")
else:
    print("Smaller than 0")


num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > num2:
    for i in range(num2, num1 + 1):
        print(i)
elif num2 > num1:
    for i in range(num1, num2 + 1):
        print(i)
else:
    print("numbers are equal")


score = int(input("Enter the score (0-100): "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
elif 0 <= score < 60:
    print("Grade: F")
else:
    print("Invalid score. Please enter a score between 0 and 100.")