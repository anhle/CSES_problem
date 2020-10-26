from bisect import bisect , insort

n,k = map(int,input().split())
a = list(map(int,input().split()))
win = a[:k]
win.sort()
for i in range(k,n):
    print(win[k//2-1]) if k%2 == 0 else print(win[k//2])
    win.pop(bisect(win,a[i-k])-1) # bisect faster than .remove()
    insort(win,a[i])

print(win[k//2-1]) if k%2 == 0 else print(win[k//2])







