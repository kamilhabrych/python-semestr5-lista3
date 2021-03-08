square = [[' '] * 10 for x in range(10)]

for x in range(10):
    for y in range(10):    
        square[x][y] = '*'

for row in square:
    print(' '.join([str(elem) for elem in row]))