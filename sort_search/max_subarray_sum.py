n = int(input())
A = list(map(int,input().split()))
# dp = [0]*n
# dp[0] = A[0]
# ans = dp[0]
# for i in range(1,n):
#     dp[i] = dp[i-1] + A[i] if dp[i-1]>0 else A[i]
#     ans=max(ans,dp[i])
#############

ans = curSumSofar = A[0]
for i in range(1,n):
    curSumSofar = (curSumSofar + A[i]) if curSumSofar>0 else A[i]
    ans = max(ans,curSumSofar)
print(ans)
