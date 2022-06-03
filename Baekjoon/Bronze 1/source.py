N = int(input())

if N <= 3 or N >= 5000:
    print(-1)

while (True):
    bag = 0
    bag, a = divmod(N, 5)
    # print(bag, a)

    bag2, b = divmod(a, 3)
    # print(bag2, b)
    bag = bag + bag2
    break

print(bag)


# 2022.05.22