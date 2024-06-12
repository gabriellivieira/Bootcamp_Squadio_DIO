capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril
valor_final = capacidade_atual + (capacidade_atual * aumento_percentual/100)

#TODO: Imprima a nova capacidade
print(f'{valor_final:.0f}')