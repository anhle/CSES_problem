import itertools
s = input()
A=[c for c in s]
ls = list(set((itertools.permutations(A))))
ans = [''.join(i) for i in ls]
print(len(ans))
for a in sorted(ans):
    print(a)
