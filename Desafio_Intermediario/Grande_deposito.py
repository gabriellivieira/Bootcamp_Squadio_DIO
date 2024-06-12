valor = float(input())

if valor > 0:
    formatado = "{:.2f}".format(valor)
    print("Deposito realizado com sucesso! \n Saldo atual: R$", formatado)
elif valor < 0:
    print("Valor invalido! Digite um valor maior que zero.")
else:
    print("Encerrando o programa...")