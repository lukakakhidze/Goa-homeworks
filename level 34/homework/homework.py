      #Uppercase
sentence = "hello world"
uppercase_sentence = sentence.upper()
print(uppercase_sentence)  

user_name = input("შეიყვანეთ თქვენი სახელი: ")
print(user_name.upper())  

def print_uppercase(strings):
    for s in strings:
        print(s.upper())

string_list = ["hello", "world", "python"]
print_uppercase(string_list)
    
    #Lowercase
sentence = "HELLO WORLD"
lowercase_sentence = sentence.lower()
print(lowercase_sentence) 

email = input("შეიყვანეთ თქვენი მეილი: ")
print(email.lower()) 

def to_lowercase(user_str):
    return user_str.lower()

user_input = "HELLO PYTHON"
print(to_lowercase(user_input))  
    
    #Capitalize
word = input("შეიყვანეთ სიტყვა: ")
print(word.capitalize())  

def capitalize_word(user_str):
    return user_str.capitalize()

input_word = "hello"
print(capitalize_word(input_word)) 