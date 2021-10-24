#include <bits/stdc++.h>
using namespace std;

bool visit[10005];
long int dis[10005];
vector<pair<long int,long int>>v[10005];
void dijkstra(){
    long int i,x,w,wt,e;
    for(i=0;i<10005;i++){
        dis[i]=INT_MAX;
        visit[i]=false;
    }
    dis[1]=0;
    multiset<pair<long int,long int>>s;
    s.insert({0,1});
    while(!s.empty()){
        pair<long int,long int>p=*s.begin();
        s.erase(s.begin());
        wt=p.first;
        x=p.second;
        if(visit[x]==true){
            continue;
        }
        visit[x]=true;
        for(i=0;i<v[x].size();i++){
            e=v[x][i].second;
            w=v[x][i].first;
            if(dis[x]+w<dis[e]){
                dis[e]=dis[x]+w;
                s.insert({dis[e],e});
            }
        }
    }
}
int main(){
    int i,j,n,m,a,b,w;
    cin>>n>>m;
    for(i=0;i<m;i++){
        cin>>a>>b>>w;
        v[a].push_back(make_pair(w,b));
    }
    dijkstra();
    for(i=2;i<=n;i++){
        cout<<dis[i]<<" ";
    }
}
