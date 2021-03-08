for x in range(5):
    for z in range(10):
        if z % 2 == 0:
            print(end=" * ")
        else:
            print(end="   ")
    print()
    for y in range(11, 1, -1):
        if y % 2 == 0:
            print(end=" * ")
        else:
            print(end="   ")
    print()
