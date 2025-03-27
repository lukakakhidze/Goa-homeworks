#list: mutable ტიპი, ელემენტების ცვლილება შესაძლებელია.
#Index: ელემენტის მდებარეობა სიის შიგნით.
#Indexing: პროცესია, რომლის დროსაც ელემენტი ხდება წვდომა ინდექსით.
#Mutable: ტიპი, რომელსაც შეიძლება შევცვალოთ შინაარსი.
#Immutable: ტიპი, რომლის შინაარსის შეცვლა შეუძლებელია.


numbers = [10, 20, 30, 40, 50]

print(numbers[0])  
print(numbers[2])  
print(numbers[4]) 


my_list = [1, "apple", 3.14, True, [1, 2], "banana", 42, None, 9.8, "cherry", False, {"key": "value"}, 100, "grape", 3, [3, 4], "orange", 200, 7.5, "mango"]

for i in range(len(my_list)):
    print(f"Element at index {i}: {my_list[i]}")


numbers = [10, 20, 30, 40, 50]

print(numbers[-5])  
print(numbers[-3]) 
print(numbers[-1]) 


name = input("Enter your name: ")

print("First symbol:", name[0])  
print("Last symbol:", name[-1])  