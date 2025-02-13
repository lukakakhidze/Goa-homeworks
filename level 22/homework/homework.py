# While ციკლი არის ერთ-ერთი ბრწყინვალე მექანიზმი, რომელიც საშუალებას აძლევს პროგრამის ნაწილის გამეორებას, სანამ გარკვეული პირობა სიმართლეა. სხვა სიტყვებით, როდესაც ციკლის პირობა ჭეშმარიტია, ის აგრძელებს შესრულებას, და როცა პირობა ყალბია, ციკლი წყდება.

#while ციკლი გამოიყენება, როდესაც უნდა გავიმეოროთ მოქმედებები მანამ, სანამ გარკვეული პირობა არის ჭეშმარიტი.


              #  while ციკლით

counter = 0  # მყარი ცვლადი, რომელიც დაიწყება 0-დან
while counter < 50:  # სანამ counter ნაკლებია 50-ისგან
    print("GOA BEST!!!")  # დაბეჭდავს ტექსტს
    counter += 1  # ზრდის counter-ს

              # for ციკლით

for i in range(50):  # 50-ჯერ გამეორება
    print("GOA BEST!!!")  # დაბეჭდავს ტექსტს


# Initialize counter variable
counter = 1

# While loop to count from 1 to 10
while counter <= 10:
    print(counter)  # Print the current value of counter
    counter += 1  # Increase counter by 1


# Initialize counter variable
counter = 2

# While loop to print even numbers between 1 and 20
while counter <= 20:
    print(counter)  # Print the current even number
    counter += 2  # Increase counter by 2 to get the next even number


# იწყება პირველი ლუწი რიცხვით
counter = 2

# while ციკლი ლუწი რიცხვების გამოსაცემად
while counter <= 20:
    print(counter)  # დაბეჭდავს ლუწ რიცხვს
    counter += 2  # ზრდის counter-ს 2-ით (რადგან რიცხვები 2-ით იზრდება)


# Initialize the counter variable to 10
counter = 10

# While loop to countdown from 10 to 1
while counter > 0:
    print(counter)  # Print the current countdown number
    counter -= 1  # Decrease the counter by 1 each time

# Print "Blast off!" after the countdown finishes
print("Blast off!")


# იწყება პირველი რიცხვით
counter = 10

# while ციკლი 10-დან 1-ის ჩათვლით რიცხვების დაბეჭდვა
while counter >= 1:
    print(counter)  # დაბეჭდავს მიმდინარე რიცხვს
    counter -= 1  # ამცირებს counter-ს 1-ით


