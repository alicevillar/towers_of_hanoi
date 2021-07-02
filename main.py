# Recursive Python function to solve tower of hanoi

# n = number of disks
# torre de origem  = from_rod
#  torre destino => to_rod
# a torre auxiliar pela qual vai passar => aux_rod


def TowerOfHanoi(n, torre_origem, torre_destino, torre_auxiliar):
    if n == 1:
        print("Move disk 1 from tower", torre_origem, "to tower", torre_destino)
        return

    TowerOfHanoi(n - 1, torre_origem, torre_auxiliar, torre_destino)

    print("Move disk", n, "from tower", torre_origem, "to tower", torre_destino)

    TowerOfHanoi(n - 1, torre_auxiliar, torre_destino, torre_origem)


# Driver code
n = 64
TowerOfHanoi(n, 'A', 'C', 'B')

# A, C, B are the name of torres
