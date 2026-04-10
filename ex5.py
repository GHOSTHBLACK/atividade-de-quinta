num = int(input("Digite um número: "))
limite = int(input("Digite o limite da tabuada (ex: 10): "))
for i in range(1, limite + 1):
    print(f"{num} x {i} = {num * i}")
