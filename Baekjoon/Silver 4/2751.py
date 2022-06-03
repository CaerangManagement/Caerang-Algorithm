import sys

num = int(sys.stdin.readline())
lst = []

while(True):
    n = int(sys.stdin.readline())
    lst.append(n)
    if len(lst) == num:
        break
lst_2 = sorted(lst)
for n in lst_2:
    print(n)
