for x in range(10+1):
    if x < 9:
        print(x,end= 4 * ' ')
    else:
        print(x,end= 3 * ' ')
print()
for i in range(1, 10+1):
    if i == 10:
        print(i, end= 2  * ' ')
    else:
        print(i, end= 3 * ' ')
    for j in range(1, 10+1):
        iloczyn = i * j
        if iloczyn < 10:
            print(end= ' ')
        print(iloczyn, end= 3 * ' ')
    print()
print()