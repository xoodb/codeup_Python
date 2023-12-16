field = []             

state_x, state_y = map(int, input().split())
for i in range(state_x):
    field.append([])
    for j in range(state_y): 
        field[i].append(0)

count = int(input())

for i in range(count):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            field[x - 1][y - 1 + j] = 1
    else:
        for j in range(l):
            field[x - 1 + j][y - 1] = 1

for i in range(state_x):
    for j in range(state_y) : 
        print(field[i][j], end=' ') 
    print()   