n,m,k = map(int,input().split())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))

cnt = 0
i,j = 0,0 # index of applicant and apartment
while i < n and j < m:
    if a[i] - k <= b[j] <= a[i]+k: # match desired size
        cnt +=1
        i,j = i+1,j+1
    elif b[j] > a[i] +k: # apartment i too big for application i
        i += 1
    elif b[j] < a[i] - k: # too small
        j += 1

print((cnt))

