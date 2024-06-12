# Lista para armazenar os itens
itens = []

#TODO: Solicite os itens ao usuário

for item in range (3):
        lista = input()
        itens.append(lista)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")