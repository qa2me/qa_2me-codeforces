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
        for(int i=0;i<n;i++){
            int e;cin>>e;
            v.push_back(e);
        }
        int m=*max_element(v.begin(),v.end());
        int mm=*min_element(v.begin(),v.end());
        cout<<(m-mm)*(n-1)<<endl;
    }
    return 0;
}
