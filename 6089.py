a, b, c = map(int, input().split())
num = a
for i in range(a, a + c - 1):
    num *= b
print(num)