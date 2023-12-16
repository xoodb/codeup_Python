a = int(input())
b = input().split()

for i in range(a):
    b[i] = int(b[i])

c = b[0]

for i in range(a):
    if(b[i] < c):
        c = b[i]

print(c)