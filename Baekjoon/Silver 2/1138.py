n = int(input())
s = list(map(int, input().split()))
a = [0 for i in range(n)]
for i in range(n + 1):
    count = 0
    k = s[i - 1]
    for j in range(0, n):
        if count == k and a[j] == 0:
            a[j] = i
            break
        if a[j] == 0:
            count += 1
for b in a:
    print(b, end = ' ')