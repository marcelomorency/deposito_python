def deposito():
    while True:
        quantia = input("O que você gostaria de depositar? $")
        if quantia.isdigit():
            quantia = int(quantia)
            if quantia > 0:
                return amount
            else:
                print("O valor deve ser maior que zero.")
        else:
            print("Por favor, digite um número válido.")

# Teste a função
valor_depositado = deposito()
print("Você depositou:", valor_depositado)
