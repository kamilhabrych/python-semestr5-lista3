for y in range(10):
    print(end=" * ")
print()
for x in range(10):
    if x == 2 or x == 9:
        print(4 * " * ", 4 * ' ', 4 * " * ")
    elif x == 3 or x == 8:
        print(3 * " * ", 10 * ' ', 3 * " * ")
    elif x == 4 or x == 7:
        print(2 * " * ", 16 * ' ', 2 * " * ")
    elif x == 5 or x == 6:
        print(1 * " * ", 22 * ' ', 1 * " * ")
for y in range(10):
    print(end=" * ")
print()
