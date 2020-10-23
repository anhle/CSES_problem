import collections
s = input()
cnt=collections.Counter(s)
res = ""
odd = 0
mid = ""
for ch in cnt:
    if cnt[ch]%2 == 0:
        res += ch*(cnt[ch]//2)
    else:
        odd += 1
        mid = ch
        if odd >= 2:
            print("NO SOLUTION")
            exit()
        res += ch*(cnt[ch]//2)
print(res + mid + res[::-1])




