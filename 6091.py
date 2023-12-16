a, b, c = map(int, input().split())
num = 1
while (not(num % a == 0 and num % b == 0 and num % c == 0)):
    num += 1
print(num)