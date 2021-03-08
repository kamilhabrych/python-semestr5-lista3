square = [[' '] * 10 for x in range(10)]

for x in range(10):
    for y in range(10):
        if x == 0 or x == 9 or y == 0 or y == 9:
            square[x][y] = '*'

for row in square:
    print(' '.join([str(elem) for elem in row]))