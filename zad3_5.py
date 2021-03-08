square = [[' '] * 10 for x in range(10)]

for x in range(10):
    for y in range(10):
        if x == 0 or x == 9 or y == 0 or y == 9:
            square[x][y] = '*'
        elif x == y:
            square[x][y] = '*'
        elif x == 1 and y == 8:
            square[x][y] = '*'
        elif x == 2 and y == 7:
            square[x][y] = '*'
        elif x == 3 and y == 6:
            square[x][y] = '*'    
        elif x == 4 and y == 5:
            square[x][y] = '*'
        elif x == 5 and y == 4:
            square[x][y] = '*'
        elif x == 6 and y == 3:
            square[x][y] = '*'
        elif x == 7 and y == 2:
            square[x][y] = '*'
        elif x == 8 and y == 1:
            square[x][y] = '*'    

for row in square:
    print(' '.join([str(elem) for elem in row]))

print()

square1 = [[' '] * 10 for x in range(10)]

for x in range(10):
    for y in range(10):
        if x == 0 or x == 9 or y == 0 or y == 9:
            square1[x][y] = '*'
        elif x == y:
            square1[x][y] = '*'

for row in square1:
    print(' '.join([str(elem) for elem in row]))