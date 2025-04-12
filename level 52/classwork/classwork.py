#codewars
#1
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


#2
def fake_bin(x):
    num = ""
    
    for i in x:
        new = int(i)
        
        if new < 5:
            num += "0"
        else:
            num += "1"
    
    return num


#3
def check(seq, elem):
    return elem in seq


#4
def string_to_array(s):
    return s.split(" ")


#5
def count_by(x, n):
    res = []
    
    for i in range(1, n+1):
        res.append(x*i)
    
    return res


#6
def reverse_seq(n):
    res = []
    
    for i in range(n, 0, -1):
        res.append(i)
    
    return res


#7
def rps(p1, p2):
    if p1 == p2: return "Draw!"

    if p1 == "scissors":
        if p2 == "rock": return "Player 2 won!"
        else: return "Player 1 won!"
    elif p1 == "rock":
        if p2 == "scissors": return "Player 1 won!"
        else: return "Player 2 won!"
    else:
        if p2 == "scissors": return "Player 2 won!"
        else: return "Player 1 won!"


#8
def count_sheep(n):
    res = ""
    for i in range(1,n+1):
        res += f"{i} sheep..."
    return res


#8
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0


#9
def get_grade(s1, s2, s3):
    number = (s1+s2+s3) / 3
    
    if number >= 90: return 'A'
    elif number >= 80: return 'B'
    elif number >= 70: return 'C'
    elif number >= 60: return 'D'
    return 'F'



