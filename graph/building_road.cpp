#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MAX=1e5+10;
vector<int> adj_list[MAX], visited(MAX,0);

void dfs(int i){
    visited[i] = 1;
    for(auto &i: adj_list[i]){
        if (!visited[i]){
             dfs(i);
        }     
    }
}
int main()
{
    int n,m;
    cin>>n>>m;

    for (int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;
        adj_list[u].push_back(v);
        adj_list[v].push_back(u);
    }
    vector<int>ans;
    for(int i =1;i<=n;i++){
        if (!visited[i]){
            ans.push_back(i);
            dfs(i);
        }
    }
    
    cout<< ans.size()-1 <<"\n";
    for(int i =0;i<ans.size()-1;i++){
        cout << ans[i] << " " <<ans[i+1] <<"\n";
    }
}

