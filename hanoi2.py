def hanoi():
    def moving(n, origin, destiny, auxiliary, move):
        def move_the_disk(start, end, move):
            print(f"Move {move:>3}: Tower {start} --> Tower {end}")
            return move + 1 # update for the next move

        if n == 1:
            move = move_the_disk(origin, destiny, move)
        else:
            move = moving(n - 1, origin, auxiliary, destiny, move)
            move = move_the_disk(origin, destiny, move)
            move = moving(n - 1, auxiliary, destiny, origin, move)

        return move

    n = int(input("How many disks do you want? \n -->"))
    print(f"Solution to the puzzle ({2 ** n - 1} moves): \n")
    moving(n, "1", "3", "2", 1)

hanoi()