#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
int main()
{

    int t;cin>>t;
    while(t--){
        vector<int> v;
        ll n;cin>>n;
        ll s=0;
        for(ll i=0;i<n-2;i++){
            ll e;cin>>e;s+=e;
        }
        ll n1;cin>>n1;s-=n1;
        ll n2;cin>>n2;s+=n2;
        cout<<s<<endl;

    }
}
