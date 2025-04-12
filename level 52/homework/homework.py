#1
def rental_car_cost(d):
    cost = d * 40
    if d >= 7:
        cost -= 50
    elif d >= 3:
        cost -= 20
    return cost


#2
def quarter_of(month):
    return (month - 1) // 3 + 1


#3
def remove_exclamation_marks(s):
    return s.replace('!', '')


#4
def get_volume_of_cuboid(length, width, height):
    return length * width * height


#5
def get_volume_of_cuboid(length, width, height):
    return length * width * height


#6
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
