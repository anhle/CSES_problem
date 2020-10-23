N=int(input())
if N == 1:
    print(1)
    exit()
if N < 4 :
    print("NO SOLUTION")
    exit()
if N == 4:
    print("2 4 1 3")
    exit()
for i in range(1,N+1,2):
    print(i)
for i in range(2,N+1,2):
    print(i)

