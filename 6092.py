a = int(input())
b = input().split()
for i in range(a):
    b[i] = int(b[i])
list = []
for i in range(24):
    list.append(0)
for i in range(a):
    list[b[i]] += 1
for i in range(1, 24):
    print(list[i], end=' ')