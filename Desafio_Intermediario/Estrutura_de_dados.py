ativos = []
quantidadeAtivos = int(input())

for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

 
ativos_ordenados = sorted(ativos, key=str.lower)

ativos_string = "\n".join(ativos_ordenados)

print(ativos_string)