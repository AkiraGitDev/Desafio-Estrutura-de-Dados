def ToH(n, A, B, C):
    if n == 1:
        print("Disk 1 from", A, "to", B)
        return
    ToH(n - 1, A, C, B)
    print("Disk", n, "from", A, "to", B)
    ToH(n - 1, C, B, A)


ToH(3, "A", "B", "C")