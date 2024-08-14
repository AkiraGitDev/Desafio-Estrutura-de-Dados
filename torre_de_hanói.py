"""Torres de Hanói. O problema consiste em mover n discos empilhados (os menores sobre os maiores), de uma haste de origem (A), para uma haste de destino (C), na mesma ordem, respeitando as seguintes regras: apenas um disco pode ser movido por vez, não colocar um disco maior sobre um menor e poder usar uma haste auxiliar (B). """

# Quantidade de discos
n = 3

# Inicializando as hastes
A = list(range(n, 0, -1))  # Haste A com discos empilhados do maior ao menor
B = []  # Haste B vazia
C = []  # Haste C vazia

# Histórico de movimentos para visualizar a solução
movimentos = []

# Uma pilha para simular a recursão manualmente
pilha = [(n, A, C, B)]

while pilha:
    # Desempilhar a próxima instrução
    discos, origem, destino, auxiliar = pilha.pop()

    if discos == 1:
        if origem:  # Verifica se a origem não está vazia
            # Movimento simples: mover um disco de 'origem' para 'destino'
            disco = origem.pop()
            destino.append(disco)
            movimentos.append((disco, origem, destino))
    else:
        # Simulando a recursão manualmente, na ordem inversa
        # Mover n-1 discos de origem para auxiliar usando destino
        pilha.append((discos - 1, auxiliar, destino, origem))
        # Mover o disco restante para o destino
        pilha.append((1, origem, destino, auxiliar))
        # Mover os n-1 discos de auxiliar para destino usando origem
        pilha.append((discos - 1, origem, auxiliar, destino))

# Exibindo os movimentos
for movimento in movimentos:
    disco, origem, destino = movimento
    origem_nome = ['A', 'B', 'C'][[A, B, C].index(origem)]
    destino_nome = ['A', 'B', 'C'][[A, B, C].index(destino)]
    print(f"Move o disco {disco} de {origem_nome} para {destino_nome}")

