import collections
def main():
    n , m = map(int , input().split())
    adj_list = collections.defaultdict(list)
    for _ in range(m):
        a , b = map(int , input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    visited = [False]*(n+1)
    def dfs(i):
        visited[i]=True
        for v in adj_list[i]:
            if not visited[v]:
                dfs(v)

    new_road = []
    for i in range(1,n+1):
        if not visited[i]:
            new_road.append(i)
            dfs(i)

    print(len(new_road)-1)
    for i in range(len(new_road)-1):
        print("{} {}".format(new_road[i],new_road[i+1]))



if __name__ == "__main__":
    main()
