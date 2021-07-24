# Recursive Python function to solve tower of hanoi

# n = number of disks

def TowerOfHanoi(n, tower_origin, tower_destiny, tower_auxiliary):
    if n == 1:
        print("Move disk 1 from tower", tower_origin, "to tower", tower_destiny)
        return

    TowerOfHanoi(n - 1, tower_origin, tower_auxiliary, tower_destiny)

    print("Move disk", n, "from tower", tower_origin, "to tower", tower_destiny)

    TowerOfHanoi(n - 1, tower_auxiliary, tower_destiny, tower_origin)

# Testing the code with 3 disks
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of the towers
