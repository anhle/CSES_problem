n = int(input())
A = list(map(int,input().split()))
total = n*(n+1)//2
for x in A:
    total -= x
print(total)