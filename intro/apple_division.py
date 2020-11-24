n = int(input())
A = (list(map(int,input().split())))

def solve(index,s1,s2):
    if index == n:
        return abs(s2-s1)
    add_to_s1 = solve(index+1,s1+A[index],s2)
    add_to_s2 = solve(index + 1 , s1 , s2+ A[index])
    return min(add_to_s1,add_to_s2)


print(solve(0,0,0))

