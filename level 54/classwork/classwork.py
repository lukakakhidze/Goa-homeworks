#1
my_info = {

    "სახელი": "ლუკა",
    "გვარი": "კახიძე",
    "ასაკი": 25,
    "საყვარელი ფერი": "შავი",
    "საცხოვრებელი ადგილი": "თბილისი",
    "hobbies": ["მუსიკა", "ფეხბურთი", "მკითხაობა"]
}

print("გასაღებები:", my_info.keys())

print("მნიშვნელობები:", my_info.values())

print("წყვილები:", my_info.items())


#2
numbers_divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print(numbers_divisible_by_3)
