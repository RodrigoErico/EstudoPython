fruits = ['banana', 'pear', 'apple', 'grape']

print(fruits[1:3])


number = [12, 3, 40, 50, 45, 78, 120, 34]

bigger_number = number[0]
for calc in number:
    if calc > bigger_number:
        bigger_number = calc

print(bigger_number)
    