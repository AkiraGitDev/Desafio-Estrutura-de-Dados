def torre_de_hanoi(numero_discos, haste_origem, haste_auxiliar, haste_destino):
  if numero_discos == 1:
    print(f"Mover o disco 1 de {haste_origem} para {haste_destino}")
    return

  torre_de_hanoi(numero_discos - 1, haste_origem, haste_destino, haste_auxiliar)
  print(f"Mover o disco {numero_discos} de {haste_origem} para {haste_destino}")
  torre_de_hanoi(numero_discos - 1, haste_auxiliar, haste_origem, haste_destino)

if __name__ == "__main__":
  numero_discos = int(input("Digite o número de discos: "))
  torre_de_hanoi(numero_discos,'A', 'B', 'C')