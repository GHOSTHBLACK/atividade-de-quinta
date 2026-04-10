import random
numero_secreto = random.randint(1, 100)
tentativas = 0
while True:
    tentativa = int(input("Adivinhe o número (1-100): "))
    tentativas += 1
    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif tentativa < numero_secreto:
        print("Maior")
    else:
        print("Menor")
