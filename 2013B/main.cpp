#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{

    int t;cin>>t;
    while(t--){
        vector<int> v;
        int n;cin>>n;
        int s=0;
        for(int i=0;i<n-2;i++){
            int e;cin>>e;s+=e;
        }
        int n1;cin>>n1;s-=n1;
        int n2;cin>>n2;s+=n2;
        cout<<s<<endl;

    }
}
