#codewars
#1 
def better_than_average(class_points, your_points):
    mean = sum(class_points) / len(class_points)
    
    if your_points > mean: return True
    return False
