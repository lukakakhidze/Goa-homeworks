numbers = (3, 7, 3, 9, 2)

print("მინიმალური:", min(numbers))
print("მაქსიმალური:", max(numbers))

first_element = numbers[0]
count_first_element = numbers.count(first_element)

print(f"პირველი ელემენტი ({first_element}) tuple-ში გვხვდება {count_first_element}-ჯერ")


def no_duplicates(user_list):
    return list(set(user_list)) 

list1 = [1, 2, 3, 2, 1, 4, 5]
list2 = ['a', 'b', 'a', 'c', 'd', 'b']
list3 = [10, 20, 30, 10, 40, 50, 20]

print(no_duplicates(list1))  
print(no_duplicates(list2))  
print(no_duplicates(list3))  
