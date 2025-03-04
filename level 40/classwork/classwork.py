def greet(name, surname, age, academy, favourite_color, city):
    result = f"Hello, my name is {name}, my surname is {surname}. I am {age} years old. I study in {academy}. My favourite color is {favourite_color}. I live in {city}."
    return result

greeting_message = greet("John", "Doe", 25, "Tech Academy", "blue", "New York")

print(greeting_message)
