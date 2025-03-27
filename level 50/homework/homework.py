#1
students_grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92,
    "David": 78
}

print("Students and their Grades:")
for student, grade in students_grades.items():
    print(f"{student}: {grade}")
print()


#2
countries_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi",
    "Australia": "Canberra"
}

print("Capitals of the countries:")
for country, capital in countries_capitals.items():
    print(capital)
print()


#3
cars = {
    "Tesla": "Model S",
    "BMW": "M3",
    "Audi": "A4",
    "Mercedes": "C-Class",
    "Toyota": "Corolla"
}

print(f"My favorite car model is: {cars['Tesla']}")
print()


#4
students_grades["Alice"] = 95

print("Updated Students' Grades:")
print(students_grades)
print()


#5
book_info = {
    "name": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}

book_info["year"] = 1926


print("Updated Book Information:")
print(book_info)
print()


#6
student_points = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92,
    "David": 78
}

average_points = sum(student_points.values()) / len(student_points)

print(f"The average points of the students is: {average_points}")
print()


#7
user_info = {}

user_info["name"] = input("Enter your name: ")
user_info["surname"] = input("Enter your surname: ")
user_info["age"] = int(input("Enter your age: "))
user_info["height"] = float(input("Enter your height in meters: "))
user_info["career"] = input("Enter your career: ")

print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key.capitalize()}: {value}")
