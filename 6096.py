field = []             

for i in range(20) :
    field.append([])
    for j in range(20) : 
        field[i].append(0) 

for i in range(19):
    place = input().split()
    for j in range(19):
        field[i][j] = int(place[j]) #왜너야
 
count = int(input())

for i in range(count) :
    x, y = map(int, input().split())
    for j in range(19):
        if field[j][y - 1] == 0:
            field[j][y - 1] = 1
        else:
            field[j][y - 1] = 0

        if field[x - 1][j] == 0:
            field[x - 1][j] = 1
        else:
            field[x - 1][j] = 0
        
for i in range(19):
    for j in range(19) : 
        print(field[i][j], end=' ') 
    print()                          