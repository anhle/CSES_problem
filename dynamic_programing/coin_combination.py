n,x = list(map(int,input().split()))
coins=list(map(int,input().split()))
##########
# bruteforce: resursive
# ans = []
# def helper(amount,subset):
#     if amount == 0:
#         ans.append(subset)
#         return
#     for i in range(len(coins)):
#         if coins[i] <= amount:
#             helper(amount-coins[i],subset+[coins[i]])
#
# helper(x,[])
####################
mod = 1000000007
dp = [0]*(x+1) # dp[i]: number of way to change amount i
dp[0] = 1
# for amount in range(1,x+1):
#     for c in coins:
#         if amount - c >= 0:
#             dp[amount] = (dp[amount] + dp[amount-c])%mod
for amount in range(min(coins),x+1):
    cnt = 0
    for c in coins:
        if amount - c >= 0:
            cnt += dp[amount-c]
    dp[amount] = cnt%mod
print(dp[x])
