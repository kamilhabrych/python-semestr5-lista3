for x in range(10+1):
    if x < 9:
        print(x,end= 5 * ' ')
    else:
        print(x,end= 4 * ' ')
print()
for i in range(1, 10+1):
    if i == 10:
        print(i, end= 2  * ' ')
    else:
        print(i, end= 3 * ' ')
    for j in range(1, 10+1):
        potega1 = j ** i
        potega2 = i ** j
        if potega1 > potega2:
            print(end= '  >   ')
        elif potega2 > potega1:
            print(end= '  <   ')
        else:
            print(end= '  =   ')
    print()
print()