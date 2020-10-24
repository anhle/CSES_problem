s = input()
visited = [[False] * 7 for i in range(7)]
ans = []


def isValid(r , c):
    return 0 <= r <= 6 and 0 <= c <= 6 and not visited[r][c]


def dfs(r , c , step):
    if r == 6 and c == 0 and step == 48:  # bottom left
        ans.append(1)
        return
    if r == 6 and c == 0 and step < 48:  # optimize1: reach target before go through all cell
        return
    visited[r][c] = True
    # print(r,c)
    if s[step] == "?" or s[step] == "U":
        if r - 1 >= 0 and not visited[r - 1][c]:
            # optimize3: if the path cannot continue forward but can turn either left or right
            if not (not isValid(r - 2 , c) and isValid(r - 1 , c - 1) and isValid(r - 1 , c + 1)):
                dfs(r - 1 , c , step + 1)
    if s[step] == "?" or s[step] == "D":
        if r + 1 <= 6 and not visited[r + 1][c]:
            if not (not isValid(r + 2 , c) and isValid(r + 1 , c - 1) and isValid(r + 1 , c + 1)):
                dfs(r + 1 , c , step + 1)
    if s[step] == "?" or s[step] == "L":
        if c - 1 >= 0 and not visited[r][c - 1]:
            if not (not isValid(r , c -2) and isValid(r + 1 , c - 1) and isValid(r - 1 , c - 1)):
                dfs(r , c - 1 , step + 1)
    if s[step] == "?" or s[step] == "R":
        if c + 1 <= 6 and not visited[r][c + 1]:
            if not (not isValid(r, c+2) and isValid(r + 1 , c + 1) and isValid(r - 1 , c + 1)):
                dfs(r , c + 1 , step + 1)

    visited[r][c] = False


dfs(0 , 0 , 0)
print(len(ans))
