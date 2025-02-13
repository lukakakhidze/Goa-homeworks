#for ციკლი არის ერთ-ერთი ყველაზე ხშირად გამოყენებული კონტროლის სტრუქტურა პროგრამირებაში, რომელიც საშუალებას იძლევა შეასრულოთ იგივე კოდის ნაწილი რამდენჯერმე გარკვეული პირობების შესაბამისად. 

for i in range(10, 31):
    print(i)

for i in range(20, 41):
    print(i)

for i in range(50, 61):
    if i % 2 == 0:
        print(i)

for i in range(10, 51):
    if i % 2 != 0:
        print(i)

sum_of_numbers = 0

for i in range(10, 21):
    sum_of_numbers += i

print(sum_of_numbers)

sum_of_even = 0

for i in range(2, 31):
    if i % 2 == 0:
        sum_of_even += i

print(sum_of_even)

