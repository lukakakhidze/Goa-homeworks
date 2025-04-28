#1
def goals(laLigaGoals, copaDelReyGoals, championsLeagueGoals):
    return laLigaGoals + copaDelReyGoals + championsLeagueGoals

#2
def double_char(string):
    return ''.join([char * 2 for char in string])

#3 
def get_age(input_string):
    return int(input_string.split()[0])

#4y
def sum_of_differences(arr):
    arr.sort(reverse=True)
    return sum(arr[i] - arr[i + 1] for i in range(len(arr) - 1))

#5
def remove_duplicates(arr):
    return list(set(arr))

#6
def points(games):
    return sum(3 if game.split(":")[0] > game.split(":")[1] else (1 if game.split(":")[0] == game.split(":")[1] else 0) for game in games)

#7
def remove_char(string):
    return string[1:-1]

#8
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        return cost - 50
    if days >= 3:
        return cost - 20
    return cost

#9
def remove_exclamation_marks(s):
    return s.replace('!', '')



#1
def array_plus_array(arr1, arr2):
    return sum(arr1 + arr2)

#2
def array_plus_array(arr1, arr2):
    return sum(arr1 + arr2)

#3
def hoop_count(n):
    return "Keep at it!" if n >= 10 else "Keep going"

#4 
def get_average(marks):
    return sum(marks) // len(marks)

#5 
def reverse_words(str):
    return ' '.join(str.split()[::-1])

