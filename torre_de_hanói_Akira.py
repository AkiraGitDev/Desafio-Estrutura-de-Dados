"""Torres de Hanói. O problema consiste em mover n discos empilhados (os menores sobre os maiores), de uma haste de origem (A), para uma haste de destino (C), na mesma ordem, respeitando as seguintes regras: apenas um disco pode ser movido por vez, não colocar um disco maior sobre um menor e poder usar uma haste auxiliar (B). """

# Quantidade de discos
n = int(input("Insira o número de discos: "))

A = list(range(n, 0, -1))
B = []
C = []

movimentos = []

pilha = [(n, A, C, B)]

while True:
    if not pilha:  # Verifica se a pilha está vazia
        break  # Sai do loop se a pilha estiver vazia
    
    discos, origem, destino, auxiliar = pilha.pop()

    if discos == 1:
        if origem:
            disco = origem.pop()
            destino.append(disco)
            movimentos.append((disco, origem, destino))
    else:
        pilha.append((discos - 1, auxiliar, destino, origem))
        pilha.append((1, origem, destino, auxiliar))
        pilha.append((discos - 1, origem, auxiliar, destino))

# Exibindo os movimentos
for movimento in movimentos:
    disco, origem, destino = movimento
    origem_nome = ['A', 'B', 'C'][[A, B, C].index(origem)]
    destino_nome = ['A', 'B', 'C'][[A, B, C].index(destino)]
    print(f"Move o disco {disco} de {origem_nome} para {destino_nome}")
