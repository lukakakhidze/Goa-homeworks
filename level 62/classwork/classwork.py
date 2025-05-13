#1
multiply = lambda side1, side2: side1 * side2

print(multiply(2, 3))  
print(multiply(5, 4))  
print(multiply(7, 8))  
print(multiply(10, 12))  
print(multiply(15, 3))  


#2
numbers = [12, 15, 7, 9, 6, 8, 20, 35, 40, 13]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
