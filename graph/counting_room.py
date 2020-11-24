def main():
    n, m = map(int,input().split())
    grid = []
    for _ in range(n):
        row = [ch for ch in input()]
        grid.append(row)

    def dfs(i , j):
        grid[i][j] = "#"
        if i-1>=0 and grid[i-1][j] == ".":
            dfs(i-1,j)
        if i+1 < n and grid[i+1][j] == ".":
            dfs(i+1,j)
        if j-1>=0 and grid[i][j-1] ==".":
            dfs(i,j-1)
        if j+1 < m and grid[i][j+1] ==".":
            dfs(i,j+1)


    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                dfs(i,j)
                cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()