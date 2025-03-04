#2
def find_python_position(sentence):
    position = sentence.find("Python")
    return position

sentence = "I love programming in Python. Python is great!"
position = find_python_position(sentence)
print(f"First occurrence of 'Python' is at index: {position}")


#3
def search_substring_in_string(string, substring):
    index = string.find(substring)
    if index != -1:
        print(f"The substring '{substring}' starts at index: {index}")
    else:
        print(f"The substring '{substring}' was not found in the string.")

input_string = "Welcome to the world of Python programming!"
substring = input("Enter the substring you want to search: ")
search_substring_in_string(input_string, substring)


#4
def find_char_index(string, char):
    index = string.find(char)
    if index != -1:
        return index
    else:
        return f"The character '{char}' is not in the string."
    
input_string = "Hello, World!"
char_to_find = input("Enter the character to search for: ")
index = find_char_index(input_string, char_to_find)
print(f"The index of '{char_to_find}' is: {index}")


#5
def count_the_occurrences(paragraph):
    count = paragraph.lower().split().count("the")
    return count

paragraph = "The quick brown fox jumps over the lazy dog. The dog was tired."
count = count_the_occurrences(paragraph)
print(f"The word 'the' appears {count} times.")


#6
def count_character_occurrences(string, char):
    count = string.count(char)
    return count

input_string = "Hello, World!"
char_to_count = input("Enter a character to count: ")
count = count_character_occurrences(input_string, char_to_count)
print(f"The character '{char_to_count}' appears {count} times in the string.")


#7
def count_word_occurrences(text, word):
    count = text.lower().split().count(word.lower())
    return count

text = "Python is awesome. Python is great for learning. I love Python!"
word_to_count = input("Enter the word you want to count: ")
count = count_word_occurrences(text, word_to_count)
print(f"The word '{word_to_count}' appears {count} times in the text.")


#8
def find_hello_index(string):
    index = string.lower().find("hello")
    if index != -1:
        print(f"The first occurrence of 'hello' is at index: {index}")
    else:
        print("The word 'hello' was not found in the string.")

input_string = "Say hello to the world! hello again!"
find_hello_index(input_string)


#9
def find_char_index(string, char):
    index = string.find(char)
    if index != -1:
        return index
    else:
        return f"The character '{char}' is not in the string."

input_string = "Hello, World!"
char_to_find = input("Enter the character to search for: ")
index = find_char_index(input_string, char_to_find)
print(f"The index of '{char_to_find}' is: {index}")


#10
def check_all_lowercase(string):
    if string.islower():
        print("All characters in the string are lowercase.")
    else:
        print("Not all characters in the string are lowercase.")

input_string = "hello world"
check_all_lowercase(input_string)


#11
def is_completely_lowercase(string):
    return string.islower()

input_string = "hello"
result = is_completely_lowercase(input_string)
print(f"Is the string completely in lowercase? {result}")


#12
def verify_lowercase_input():
    user_input = input("Please enter a string: ")
    
    if user_input.islower():
        print("The string contains only lowercase letters.")
    else:
        print("The string does not contain only lowercase letters.")

verify_lowercase_input()


#13
def check_all_uppercase(string):
    if string.isupper():
        print("All characters in the string are uppercase.")
    else:
        print("Not all characters in the string are uppercase.")

input_string = input("Enter a string: ")
check_all_uppercase(input_string)


#14
def is_completely_uppercase(string):
    return string.isupper()

input_string = input("Enter a string: ")
result = is_completely_uppercase(input_string)
print(f"Is the string completely uppercase? {result}")


#15
def check_user_string_uppercase():
    user_input = input("Please enter a string: ")
    
    if user_input.isupper():
        print("The string is in uppercase.")
    else:
        print("The string is not in uppercase.")

check_user_string_uppercase()

def remove_one_element(lst, index):
    del lst[index]  
    print(lst)  

my_list = [10, 20, 30, 40, 50]
remove_one_element(my_list, 2)
