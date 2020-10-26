import collections
n = int(input())
a = list(map(int,input().split()))
cnt = collections.Counter(a)
print(len(cnt))
