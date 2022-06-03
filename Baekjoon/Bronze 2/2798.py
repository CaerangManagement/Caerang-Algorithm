#2798 블랙잭 05 / 08

n, m = map(int, input().split())
nums = list(map(int, input().split()))

sumNum = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] > m:
                continue
            else:
                sumNum = max(sumNum, nums[i] + nums[j] + nums[k])
print(sumNum)
