matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matriz[1][0]) # 4

# for encadeado

for i in range(3):
    for e in range(3):
        print(matriz[i][e])
        
for linha in matriz:
    print(linha)
