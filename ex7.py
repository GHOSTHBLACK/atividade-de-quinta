while True:
    n = int(input("Digite a quantidade N (maior que 0): "))
    if n > 0:
        break
    else:
        print("N deve ser maior que 0.")
numeros = []
for i in range(n):
    num = float(input(f"Digite o número {i+1}: "))
    numeros.append(num)
maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / n
print(f"Maior: {maior}, Menor: {menor}, Média: {media}")
