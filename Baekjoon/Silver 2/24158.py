def search(arr,dp):
    x = 0
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
             if arr[i] > arr[j]:
                 x = dp[j]+1
                 dp[i] = max(x,dp[i])

arr = [int(input()) for i in range(int(input()))]
dp = [1]*len(arr)   #자기 자신 포함 

search(arr,dp)    
print(max(dp))