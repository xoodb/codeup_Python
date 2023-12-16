field = []             

for i in range(10) :
    field.append([])
    for j in range(10) : 
        field[i].append(0) 

for i in range(10):
    place = input().split()
    for j in range(10):
        field[i][j] = int(place[j])

x = 1; y = 1

while True:
    if field[x][y] == 0:
        field[x][y] = 9
    elif field[x][y] == 2:
        field[x][y] = 9
        break
    if (field[x][y + 1] == 1 and field[x + 1][y] == 1):
        break
    if field[x][y + 1] != 1: #순서중요! 오른쪽으로 이동 불가시 아래로 이동
        y += 1
    elif field[x + 1][y] != 1:
        x += 1

for i in range(10):
    for j in range(10) : 
        print(field[i][j], end=' ') 
    print()      