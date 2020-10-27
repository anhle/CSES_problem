import bisect
n = int(input())
A = list(map(int,input().split()))
towers = []
for x in A:
    # search for index i such that all value towers[i]< x
    i = bisect.bisect(towers,x)
    if i < len(towers):# not found
        towers[i] = x
    else:
        towers.append(x)

print(len(towers))

