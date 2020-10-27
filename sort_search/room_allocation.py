# Note: wrong answer
import bisect
import collections

n = int(input())
A = []
for i in range(n):
    a = list(map(int , input().split()))
    A.append(a + [i])
A.sort(key=lambda x: x[1])  # sort by arrival
rooms = []  # keep track the latest departure
ans = [-1] * n
for i in range(len(A)):
    # all left side[:i] val new arrival
    r = bisect.bisect_left(rooms , A[i][0])
    if r != 0:  # found
        r -= 1
        ans[A[i][2]] = r + 1  # adjust index to room
        rooms[r] = A[i][1]
    else:
        rooms.append(A[i][1]) # asign new room
        ans[A[i][2]]=len(rooms)

print(len(rooms))
for r in ans:
    print(r , end=' ')
