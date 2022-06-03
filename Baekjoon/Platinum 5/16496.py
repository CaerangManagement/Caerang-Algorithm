n,arr = input(),input().split()
print(int("".join(list(zip(*sorted([(int((arr[i]*10)[:10]),arr[i]) for i in range(int(n))],key=lambda x: -x[0])))[1])))

'''
위 코드는 최대한 압축해서 만든 숏코딩
n = input()
arr = list(map(int,input().split()))
arrC = []
result = ""
cnt = 0
for i in arr:
    x = str(i)
    while len(x) <= 10 : x+=x
    arrC.append((int(x[:10]),cnt))
    cnt+=1
for i in sorted(arrC,key=lambda x: -x[0]):
    result+=str(arr[i[1]])
print(result if int(result) != 0 else 0)
'''