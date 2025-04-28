#1
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Isaac", "John"]

renewed = [name for name in names if len(name) < 6 or name[0] == 'A']

print(renewed)


#2
try:
    user_input = input("გთხოვთ შეიყვანოთ რიცხვი: ")
    number = int(user_input)  
    print(number)
except:
    print("error") 