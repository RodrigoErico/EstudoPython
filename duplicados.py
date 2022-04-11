# retirar os numeros duplicados

num = [1, 2, 34, 24, 4, 3, 4, 30 , 2, 40]

num_limpa = []

for numbers in num:
    if numbers not in num_limpa:
        num_limpa.append(numbers)
        
print(num_limpa)
