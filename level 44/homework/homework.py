# 1) Convert a Number to a String!
def number_to_string(num):
    return str(num)  # გარდაქმნის რიცხვს სტრიქონად

# 2) Summation
def summation(num):
    return sum(range(1, num + 1))  # ითვლის 1-დან num-მდე რიცხვების ჯამს

# 3) Function 1 - hello world
def greet():
    return "hello world!"  # აბრუნებს სტრიქონს "hello world!"

# 4) Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)  # ითვლის True მნიშვნელობებს სიაში

# 5) Remove String Spaces
def no_space(x):
    return x.replace(" ", "")  # შლის ყველა გამოტოვებულ ადგილს სტრიქონიდან

# 6) You Can't Code Under Pressure #1
def double_integer(i):
    return i * 2  # აბრუნებს რიცხვის გაორმაგებულ მნიშვნელობას

# 7) Returning Strings
def greet(name):
    return f"Hello, {name} how are you doing today?"  # ქმნის მისალმების ტექსტს

# 8) Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)  # გარდაქმნის ბულიან ტიპს სტრიქონად

# 9) Basic Mathematical Operations
def basic_op(operator, value1, value2):
    return eval(f"{value1} {operator} {value2}")  # ასრულებს მათემატიკურ ოპერაციას

# 10) Keep Hydrated!
def litres(time):
    return time // 2  # თითო საათზე იღებს 0.5 ლიტრ წყალს

# 11) Century From Year
def century(year):
    return (year + 99) // 100  # ითვლის საუკუნეს წლიდან

# 12) Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo"


