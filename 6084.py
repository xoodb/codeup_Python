h, b, c, s = map(int, input().split())
bit = (h * b * c * s)
print('%.1f MB' %(bit / 8 / 1024 / 1024))