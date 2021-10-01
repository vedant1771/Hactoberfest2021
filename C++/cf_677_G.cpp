/*Author- Soumak Poddar*/
//Problem link - http://codeforces.com/contest/1433/problem/G

#include<bits/stdc++.h>
using namespace std;

#define ll long long int
#define sll signed long long int
#define ull unsigned long long int
#define umax uintmax_t

#define um unordered_map
#define us unordered_set
#define mm multimap
#define pq priority_queue
#define pi pair<int,int>
#define vi vector<int>
#define vll vector<ll>
#define gi greater<int>

#define mp make_pair
#define pb push_back
#define fir first
#define sec second
#define M 1000000007

template<typename T>
T gcd(T a,T b)
{
   if(a==0)
      return b;
   return gcd(b%a,a);
}
template<typename T>
T lcm(T a,T b)
{
   T g=gcd<T>(a,b);
   return (a*b)/g;
}
template<typename T>
bool isprime(T n)
{
   if(n<=1)
      return false;
   for(int i=2;i<sqrt(n);i++)
      if(n%i==0)
         return false;
   return true;
}
vector<bool> prime;
void seive(ll n)
{
   prime.resize(n+1);
   fill(prime.begin(),prime.end(),true);
   prime[0]=prime[1]=false;
   for(int i=2;i*i<=n;i++)
   {
      if(prime[i]==true)
      {
         for(int j=i*i;j<=n;j+=i)
            prime[j]=false;
      }
   }
}

void solve();
int main()
{
   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
   cout.tie(NULL);

   #ifndef ONLINE_JUDGE
      freopen("input.txt", "r", stdin);
      freopen("error.txt", "w", stderr);
      freopen("output.txt", "w", stdout);
   #endif
   
   int t=1;
   // cin>>t;
   while(t--)
   {
      solve();
      cout<<"\n";
   }
   cerr<<"Time Taken : "<<(float)clock()/CLOCKS_PER_SEC<<" secs"<<endl;
   return 0;
}

vector<vector<pair<int,int>>> adj;
vector<vi> d;
vector<vi> routes;
int n,m,k;

void dijk(int i)
{
   set<pair<int,int>> s;
   d[i][i]=0;
   s.insert({0,i});

   while(!s.empty())
   {
      int x=s.begin()->sec;
      s.erase(s.begin());

      for(auto j:adj[x])
      {
         int w=j.sec;
         int y=j.fir;
         if(d[i][y]>d[i][x]+w)
         {
            s.erase({d[i][y],y});
            d[i][y]=d[i][x]+w;
            s.insert({d[i][y],y});
         }
      }
   }
}

int get(int i,int j)
{
   int ans=0;

   for(auto a:routes)
      ans+=min({d[a[0]][a[1]],d[a[0]][i]+d[j][a[1]],d[j][a[0]]+d[a[1]][i]});

   return ans;
}

void solve()
{
   int n,m,k;
   cin>>n>>m>>k;

   adj.resize(n+1);
   vector<vi> edg;

   while(m--)
   {
      int x,y,w;
      cin>>x>>y>>w;
      adj[x].pb({y,w});
      adj[y].pb({x,w});
      edg.pb({x,y});
   }

   d.assign(n+1,vi(n+1,INT_MAX));

   while(k--)
   {
      int a,b;
      cin>>a>>b;
      routes.pb({a,b});
   }

   int ans=INT_MAX;

   for(int i=1;i<=n;i++)
      dijk(i);

   for(auto i:edg)
   {
      ans=min(ans,get(i[0],i[1]));
   }

   cout<<ans;
}