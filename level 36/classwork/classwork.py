def check_lowercase(user_str):
    print(user_str == user_str.lower())

text = input("Enter sentence: ")
check_lowercase(text)


def iscapitalized(user_str):
    print(user_str[0].isupper() and user_str[1:].islower())

text = input("შეიყვანეთ წინადადება: ")

iscapitalized(text)


def manual_isdigit(user_str):
    for char in user_str:
        if char not in "0123456789":
            print(False)
            return
    print(True)

text = input("შეიყვანეთ ტექსტი: ")

manual_isdigit(text)


def split_sentence(user_str):
    print(user_str.split())

text = input("შეიყვანეთ ტექსტი: ")

split_sentence(text)


