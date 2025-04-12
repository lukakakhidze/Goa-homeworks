# 1
def number_to_string(num):
    return str(num)  

# 2
def summation(num):
    return sum(range(1, num + 1))  

# 3
def greet():
    return "hello world!"  

# 4
def count_sheeps(sheep):
    return sheep.count(True) 

# 5
def no_space(x):
    return x.replace(" ", "")  

# 6
def double_integer(i):
    return i * 2  

# 7
def greet(name):
    return f"Hello, {name} how are you doing today?"  

# 8
def boolean_to_string(b):
    return str(b)  

# 9
def basic_op(operator, value1, value2):
    return eval(f"{value1} {operator} {value2}")  

# 10
def litres(time):
    return time // 2  

# 11
def century(year):
    return (year + 99) // 100  

# 12
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo"



#codewars
# 3
def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)

# 4
def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2 == 1

# 5
def sum_array(a):
    return sum(a)

# 6
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

# 7
def make_upper_case(s):
    return s.upper()
