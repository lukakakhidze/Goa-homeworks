# ცვლადები სხვადასხვა ტიპით
name = "luka"  
age = 30  
height = 5.9  
is_student = False  
courses = ["Math", "Science", "History"]  

# შემოწმება: თითოეული ცვლადის მონაცემთა ტიპი
print(type(name))  
print(type(age))  
print(type(height))  
print(type(is_student)) 
print(type(courses))  

# მომხმარებლისგან ორი რიცხვის მიღება
num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
num2 = float(input("შეიტანეთ მეორე რიცხვი: "))

# ჯამი, სხვაობა, ნამრავლი და განაყოფი
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2

# შედეგების დაბეჭდვა
print("ჯამი: ", sum_result)
print("სხვაობა: ", difference_result)
print("ნამრავლი: ", product_result)
print("განაყოფი: ", quotient_result)