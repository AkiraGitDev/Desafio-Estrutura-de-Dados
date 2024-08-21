def hanoi(n, origem, destino, suporte):
    if n == 1:
        print(f"Mova o disco 1 da haste {origem} para a haste {destino}")
        return

    # Mover n-1 discos da haste origem para a haste suporte
    hanoi(n-1, origem, suporte, destino)
    # Mover o disco n para a haste destino
    print(f"Mova o disco {n} da haste {origem} para a haste {destino}")
    # Mover os n-1 discos da haste suporte para a haste destino
    hanoi(n-1, suporte, destino, origem)

def resolver_torre_de_hanoi():
    discos = int(input("Quantos discos? "))
    
    origem = 1
    destino = 3
    suporte = 2

    print(f"Resolvendo Torre de Hanói com {discos} discos e 3 hastes:")
    hanoi(discos, origem, destino, suporte)
    