#include <bits/stdc++.h>
using namespace std;
void DFS(int node, vector<int> adj[], vector<int> &vis, vector<int> &dfs)
{
    dfs.push_back(node);
    vis[node] = 1;
    for (auto it : adj[node])
    {
        if (vis[it] == 0)
        {
            DFS(it, adj, vis, dfs);
        }
    }
}

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> adj[n + 1];
    for (int i = 1; i <= m; i++)
    {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    cout << "Adjacency List\n";
    for (int i = 1; i <= n; i++)
    {
        cout << i << "->";
        for (auto it : adj[i])
        {
            cout << it << " ";
        }
        cout << endl;
    }
    vector<int> vis(n + 1, 0);
    vector<int> dfs;
    for (int i = 1; i <= n; i++)
    {
        if (vis[i] == 0)
        {
            DFS(i, adj, vis, dfs);
        }
    }
    cout << "DFS is: ";
    for (auto it : dfs)
    {
        cout << it << " ";
    }
    cout << endl;
}
