w, h, b = map(int, input().split())
bit = (w * h * b)
print('%.2f MB' %(bit / 8 / 1024 / 1024))