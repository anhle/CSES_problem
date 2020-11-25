#include <bits/stdc++.h> 
using namespace std; 

#define ff first
#define ss second
#define pb push_back
#define pii pair< int,int >
#define fast ios::sync_with_stdio(0) , cin.tie(0) , cout.tie(0) ;

void dfs(vector<vector<bool>> &visited,vector<vector<char>> &grid,int i, int j, int n, int m){
    visited[i][j] = 1;
    if(i+1 < n && !visited[i+1][j] && grid[i+1][j]=='.')
        dfs(visited,grid,i+1,j,n,m);
    if(i-1 >=0 && !visited[i-1][j] && grid[i-1][j]=='.')
        dfs(visited,grid,i-1,j,n,m);
    if(j+1 < m && !visited[i][j+1] && grid[i][j+1]=='.')
        dfs(visited,grid,i,j+1,n,m);
    if(j-1 >= 0 && !visited[i][j-1] && grid[i][j-1]=='.')
        dfs(visited,grid,i,j-1,n,m);
    
}
int main()
{
    // A fast IO program
    fast;

    int n,m;
    cin >> n >>m;

    vector<vector<char>> grid(n,vector<char>(m));
    vector<vector<bool>> visited(n,vector<bool>(m,0));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++)
        {
           cin>>grid[i][j];
        }
    }
    int cnt = 0;
    for (int i = 0; i < n; i++){
       for(int j = 0; j< m;j++){
           if(! visited[i][j] && grid[i][j]=='.'){
               cnt++;
               dfs(visited,grid,i,j,n,m);
           }
       }
    }
    cout <<cnt;
    
}