
def deposit():
    while True:
        amount = input("O que você gostaria de depositar? $")
        if amount.isdigit():
           amount = int(amount)
           if amount > 0:
              break
           else:
             print("O quantia ele tem que ser maior do que zero.")
        else:
             print("Porfavor digite um número.")

    return amount         

deposit()
