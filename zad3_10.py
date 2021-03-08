square = [[' '] * 10 for x in range(10)]

for x in range(10):
    for y in range(10):
        if (x == 0 or x == 9) and y > 2 and y < 7:    
            square[x][y] = '*'
        elif (x == 1 or x == 8) and (y == 2 or y == 7):
            square[x][y] = '*'
        elif (x == 2 or x == 7) and (y == 1 or y == 8):
            square[x][y] = '*'
        elif (y == 0 and x > 2 and x < 7) or (y == 9 and x > 2 and x < 7):
            square[x][y] = '*'
        else:
            square[x][y] = ' '

for row in square:
    print(' '.join([str(elem) for elem in row]))

square1 = [[' '] * 10 for x in range(10)]

print()

for x in range(10):
    for y in range(10):
        if (x == 0 or x == 9) and y > 2 and y < 7:    
            square1[x][y] = '*'
        elif (x == 1 or x == 8) and y > 1 and y < 8:
            square1[x][y] = '*'
        elif (x == 2 or x == 7) and y > 0 and y < 9:
            square1[x][y] = '*'
        elif x > 2 and x < 7:
            square1[x][y] = '*'
        else:
            square1[x][y] = ' '

for row in square1:
    print(' '.join([str(elem) for elem in row]))