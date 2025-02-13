# შექმენი ცვლადი correct_num და მიეცი მნიშვნელობა 10
correct_num = 10

# დაიწყო ციკლი, რომელიც გთხოვს მომხმარებელს რიცხვის შეყვანას
while True:
    # მომხმარებლის შეყვანა
    guess = int(input("შეიყვანეთ მთელი რიცხვი: "))
    
    # შედარება correct_num-თან
    if guess == correct_num:
        print("correct guess")  # სწორი პასუხი
        break  # ციკლის შეწყვეტა
    else:
        print("არასწორი პასუხი, სცადეთ კვლავ.")

