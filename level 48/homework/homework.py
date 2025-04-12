#codewars
#1
def count_positives_sum_negatives(arr):
    if arr == [] or arr == None: return []
    
    count_of_pos = 0
    sum_of_neg = 0
    
    for i in arr:
        if i > 0: count_of_pos += 1
        else: sum_of_neg += i
    
    return [count_of_pos, sum_of_neg]


#2
def dna_to_rna(dna):
    return dna.replace("T", "U")


#3
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump: return True
    return False


#4
def bmi(weight, height):
    res = weight / height ** 2
    
    if res <= 18.5: return "Underweight"
    elif res <= 25.0: return "Normal"
    elif res <= 30.0: return "Overweight"
    return "Obese"