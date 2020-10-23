n = int(input())
A = (list(map(int,input().split())))
total = sum(A)
ans = 0
for i in range(1<<n):
    cumSum = 0
    for j in range(n):
        if (i>>j)&1:
            cumSum += A[j]
        if cumSum <= total//2:
            ans = max(ans,cumSum)
print(total - 2*ans)

