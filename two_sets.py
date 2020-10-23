n = int(input())
sum = n*(n+1)//2
if sum%2 != 0:
    print("NO")
    exit()
print(("YES"))
subset1,subset2 = [],[]
idx = n
target = sum//2
while idx < target:
    subset1.append(idx)
    target -= idx
    idx -= 1
subset1.append(target)
print(len(subset1))
for x in subset1:
    print(x,end=' ')
print("")
print(n - len(subset1))
for i in range(idx,0,-1):
    if i != target:
        print(i,end=" ")



