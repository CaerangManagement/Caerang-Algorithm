# 1357

x, y = map(str, input().split())
z = str(int(x[::-1]) + int(y[::-1]))
print(int(z[::-1]))
