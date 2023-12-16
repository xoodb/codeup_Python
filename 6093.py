a = int(input())
b = input().split()

for i in range(a):
    b[i] = int(b[i])
    
list = []

for i in range(a, 0, -1):
    list.append(b[i - 1])

for i in range(a):
    print(list[i], end=' ')