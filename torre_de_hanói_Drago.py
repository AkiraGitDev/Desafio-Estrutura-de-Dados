# Função para resolver o problema das Torres de Hanói versão humildade
def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 da haste {origem} para a haste {destino}")
    else:
        hanoi(n - 1, origem, auxiliar, destino)
        print(f"Mova o disco {n} da haste {origem} para a haste {destino}")
        hanoi(n - 1, auxiliar, destino, origem)

# Solicita ao usuário o número de discos
n = int(input("Digite o número de discos: "))

# Chama a função hanoi com os valores fornecidos pelo usuário
hanoi(n, 'A', 'C', 'B')

"""A: Haste de origem — onde os discos começam.
   C: Haste de destino — onde queremos que os discos terminem.
   B: Haste auxiliar — usada como apoio temporário durante os movimentos."""