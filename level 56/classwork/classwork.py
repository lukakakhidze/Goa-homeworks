#1
def update_light(current):
    next_light = {
        "green": "yellow",
        "yellow": "red",
        "red": "green"
    }
    return next_light[current]


#2
def battle(x, y):
    score_x = sum(ord(c) - 64 for c in x)
    score_y = sum(ord(c) - 64 for c in y)
    if score_x > score_y:
        return "Left side wins!"
    elif score_x < score_y:
        return "Right side wins!"
    else:
        return "Let's fight again!"
    

#3
def digitize(n):
    return [int(d) for d in str(n)][::-1]


#4
def sum_mix(arr):
    return sum(int(x) for x in arr)


#5
def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


#6
def get_sum(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))


#7
def is_uppercase(inp):
    return inp == inp.upper()


#8
def sum_digits(number):
    return sum(int(d) for d in str(abs(number)))


#9
def counter_effect(hit_count):
    return [[int(d) + i for i in range(10 - int(d))] for d in hit_count]