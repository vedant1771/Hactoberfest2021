#include<bits/stdc++.h>
using namespace std;
#define ll long long int

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    ll t, n;
    float k;
    cin >> t;
    while(t--) {
        cin >> n >> k;
        vector<ll> res(32,0);
        ll x, count=0;
        while(n--) {
            cin >> x;
            int pos = 31;
            while(x != 0) {
                res[pos] += (x%2);
                x /= 2;
                pos--;
            }
        }
        
        res.erase(remove(res.begin(), res.end(), 0), res.end());
        
        for(auto a:res) {
            if(a != 0) {
                float d = a/k;
                count += ceil(d);
            }
        }
        
        cout << count << "\n";
    }

    return 0;
}
